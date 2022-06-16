from typing import List, Literal, Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.conf import settings
from datetime import timedelta
from redis import StrictRedis
from requests_cache import CachedSession


from FreiRui.views.category.get_categories import get_categories
from FreiRui.models.Categories import Categories
from FreiRui.models.Posts import Posts
from FreiRui.settings import MODELTRANSLATION_FALLBACK_LANGUAGES

# redis_cache = StrictRedis.from_url(REDIS_URL)
session = CachedSession(
    'youtube_rss',
    # Save files in the default user cache dir
    use_cache_dir=True,
    # Use Cache-Control headers for expiration, if available
    cache_control=True,
    # Otherwise expire responses after one day
    expire_after=timedelta(minutes=15),
    # Cache POST requests to avoid sending the same data twice
    allowable_methods=['GET', 'POST'],
    allowable_codes=[200],
    # Match all request headers
    match_headers=False,
    # In case of request errors, use stale cache data if possible
    stale_if_error=True,
    # Use the redis cache backend
    backend='redis',
    host=f"{settings.REDIS_HOST}",
    port=int(settings.REDIS_PORT),
    password=settings.REDIS_PASSWORD,
)


def get_fallback(lang: str):
    default_fallback = ('pt', 'en', 'de')
    de_fallback = MODELTRANSLATION_FALLBACK_LANGUAGES.get(
        'de') or default_fallback
    en_fallback = MODELTRANSLATION_FALLBACK_LANGUAGES.get(
        'en') or default_fallback
    pt_fallback = MODELTRANSLATION_FALLBACK_LANGUAGES.get(
        'default') or default_fallback
    name_lang = f'name_{lang}'
    if lang == 'de':
        fallback: List[str] = [*de_fallback]
    elif lang == 'en':
        fallback = [*en_fallback]
    else:
        fallback = [*pt_fallback]
        name_lang = 'name'
    return name_lang, fallback


def category_by_name(lang: str, category_name: str, is_authenticated: bool) -> Union[Categories, None]:
    if not category_name:
        return None
    [name_lang, fallback] = get_fallback(lang)
    try:
        options = {name_lang: category_name} if is_authenticated else {
            name_lang: category_name, 'published': True}
        category = Categories.objects.get(
            **options,
        )
        return category
    except Categories.DoesNotExist:
        category = None
    while fallback:
        if lang in fallback:
            fallback.remove(lang)
        lang = fallback[0] if len(fallback) > 0 else None
        if lang is None:
            break
        try:
            name_lang = f'name_{lang}'
            options = {name_lang: category_name} if is_authenticated else {
                name_lang: category_name, 'published': True}
            category = Categories.objects.get(
                **options,
            )
            # if category is not found, will jump to exception
            return category
        except Categories.DoesNotExist:
            category = None
    return category or None


def post_list(
        request: HttpRequest,
        category: str,
        categories: List[Categories] = None) -> HttpResponse:
    if categories is None:
        categories = get_categories(request)
    category = category.replace('_', ' ') if category else categories[0].name
    lang = request.COOKIES.get('lang', 'pt')
    prev_lang = request.COOKIES.get('prev_lang', '')
    if lang == prev_lang:
        prev_lang = ''
    original_lang = lang
    posts = None
    fallback = get_fallback(lang)[1]
    while not posts and fallback:
        # print(f'iteration {lang}')
        if (lang in fallback):
            fallback.remove(lang)
        category_name = 'category__name' if lang == 'pt' else f'category__name_{prev_lang or lang}'
        if (request.user.is_authenticated):
            posts: List[Posts] = Posts.objects.filter(
                **{category_name: category}
            ).order_by('published_date')
        else:
            posts: List[Posts] = Posts.objects.filter(
                **{category_name: category,
                    "category__published": True,
                    "is_deleted": False,
                    "published_date__lte": timezone.now()
                   }
            ).order_by('published_date')
        lang = fallback[0] if len(fallback) > 0 else None
    lang = original_lang
    # [print(category.__dict__) for category in categories]
    _category = category_by_name(lang, category, request.user.is_authenticated)
    youtube_rss = ''
    post_type: Union[Literal['cards'], Literal['accordion'],
                     Literal['single'], Literal['youtube']] = 'cards'
    if _category and _category.listing_type == 'accordion':
        post_type = 'accordion'
    elif _category and _category.listing_type == 'single':
        post_type = 'single'
        if len(posts) > 0:
            posts: Posts = posts[0]
    elif _category and _category.listing_type == 'youtube':
        post_type = 'youtube'
        youtube_url = _category and _category.video_url
        if youtube_url:
            # import time
            # start = time.time()
            youtube_rss = session.get(
                f'https://www.youtube.com/feeds/videos.xml?channel_id={youtube_url}'
            ).text
            # end = time.time()
            # print(f'{end - start} seconds')

    return render(request, f'post/list_{post_type}.html', {
        'posts': posts,
        'categories': categories,
        'category': _category,
        'youtube_rss': youtube_rss,
        'now': timezone.now()
    })

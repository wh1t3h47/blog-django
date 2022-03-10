from typing import List, Literal, Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from requests_cache import CachedSession

from FreiRui.models.Categories import Categories
from FreiRui.models.Posts import Posts

session = CachedSession(
    'youtube_rss',
    use_cache_dir=True,                 # Save files in the default user cache dir
    cache_control=True,                 # Use Cache-Control headers for expiration, if available
    expire_after=timedelta(minutes=15), # Otherwise expire responses after one day
    allowable_methods=['GET', 'POST'],  # Cache POST requests to avoid sending the same data twice
    allowable_codes=[200],
    match_headers=True,                 # Match all request headers
    stale_if_error=True,                # In case of request errors, use stale cache data if possible
)

def post_list(request: HttpRequest, category: str) -> HttpResponse:
    if (request.user.is_authenticated):
        categories: List[Categories] = Categories.objects.order_by('order')
        posts: List[Posts] = Posts.objects.filter(
        category__name=category,
        ).order_by('published_date')
    else:
        categories: List[Categories] = Categories.objects.filter(published=True, ).order_by('order')
        posts: List[Posts] = Posts.objects.filter(
        category__name=category,
        category__published=True,
        is_deleted=False,
        published_date__lte=timezone.now()).order_by('published_date')
    category = Categories.objects.get(name=category.replace('_', ' '))
    youtube_rss = ''
    post_type: Union[Literal['cards'], Literal['accordion'], Literal['single'], Literal['youtube']] = 'cards'
    if category.listing_type == 'accordion':
        post_type = 'accordion'
    elif category.listing_type == 'single':
        post_type = 'single'
        if len(posts) > 0:
          posts: Posts = posts[0]
    elif category.listing_type == 'youtube':
        post_type = 'youtube'
        youtube_url = category.video_url
        if youtube_url:
            # import time
            # start = time.time()
            youtube_rss = session.get(f'https://www.youtube.com/feeds/videos.xml?channel_id={youtube_url}').text
            # end = time.time()
            # print(f'{end - start} seconds')

    return render(request, f'post/list_{post_type}.html', {'posts': posts, 'categories': categories, 'category': category, 'youtube_rss': youtube_rss, 'now': timezone.now()})

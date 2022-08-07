from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect

from FreiRui.views.post.list import post_list
from FreiRui.views.category.get_categories import get_categories
from FreiRui.views.category.new import category_new


def index(request: HttpRequest) -> HttpResponse:
    lang = request.COOKIES.get('lang', 'pt')
    categories = get_categories(request)
    # print(categories)
    if len(categories) > 0:
        category = categories[0]
        if lang == 'de':
            category_translated = (
                category.__dict__['name_de']
                or category.__dict__['name_en']
                or category.__dict__['name']
            )
        elif lang == 'en':
            category_translated = (
                category.__dict__[f'name_en']
                or category.__dict__['name']
            )
        else:
            category_translated = category.__dict__['name']
        posts_view = post_list(request,
                               category_translated,
                               categories)
        return posts_view
    # else:
    if request.user.is_authenticated:
        return category_new(request)
    # else:
    return redirect('/admin')

from typing import List
from django.http.request import HttpRequest

from FreiRui.models.Categories import Categories


def normalize_categories(categories: List[Categories], lang: str) -> List[Categories]:
    _categories: List[Categories] = []
    if lang == 'de':
        for category in categories:
            category.name = category.name_de or category.name_en or category.name
            _categories.append(category)
    elif lang == 'en':
        for category in categories:
            category.name = category.name_en or category.name
            _categories.append(category)
    else:  # pt
        _categories = categories
    return _categories


def get_categories(request: HttpRequest) -> List[Categories]:
    lang = request.COOKIES.get('lang', 'pt')
    if (request.user.is_authenticated):
        categories = normalize_categories(
            Categories.objects.order_by('order'),
            lang
        )
    else:
        categories = normalize_categories(Categories.objects.filter(
            **{'published': True},
        ).order_by('order'), lang)
    # only categories that have category.name
    valid_categories = [category for category in categories if category.name]
    return valid_categories

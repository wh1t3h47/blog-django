from typing import List, Literal, Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from FreiRui.models.Category import Category
from FreiRui.models.Post import Post


def post_list(request: HttpRequest, category: str) -> HttpResponse:
    categories: List[Category] = Category.objects.filter(published=True, ).order_by('order')
    category = Category.objects.get(name=category)
    posts: List[Post] = Post.objects.filter(
        category__name=category,
        category__published=True,
        is_deleted=False,
        published_date__lte=timezone.now()).order_by('published_date')
    post_type: Union[Literal['cards'], Literal['accordion']] = 'cards'
    if category.listing_type == 'accordion':
        post_type = 'accordion'
    return render(request, f'post/list_{post_type}.html', {'posts': posts, 'categories': categories})

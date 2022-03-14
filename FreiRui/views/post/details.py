from typing import List
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from FreiRui.models.Categories import Categories
from FreiRui.models.Posts import Posts


def post_details(request: HttpRequest, category: str, pk: str) -> HttpResponse:
    category = category.replace('_', ' ')
    if (request.user.is_authenticated):
        categories: List[Categories] = Categories.objects.order_by('order')
    else:
        categories: List[Categories] = Categories.objects.filter(
            published=True, ).order_by('order')
    post = get_object_or_404(Posts, category__name=category, pk=pk)
    return render(request, 'post/details.html', {'post': post, 'categories': categories})

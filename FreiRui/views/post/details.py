from typing import List
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from FreiRui.models.Category import Category
from FreiRui.models.Post import Post


def post_details(request: HttpRequest, category: str, pk: str) -> HttpResponse:
    categories: List[Category] = Category.objects.filter(published=True, ).order_by('order')
    post = get_object_or_404(Post, category__name=category, pk=pk)
    return render(request, 'post/details.html', {'post': post, 'categories': categories})

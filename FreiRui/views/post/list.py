from typing import List
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from FreiRui.models.Post import Post


def post_list(request: HttpRequest, category: str) -> HttpResponse:
    posts: List[Post] = Post.objects.filter(
        category__name=category,
        category__published=True,
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post/list.html', {'posts': posts})

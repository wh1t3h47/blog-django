from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from FreiRui.models.Post import Post


def post_details(request: HttpRequest, category: str, pk: str) -> HttpResponse:
    post = get_object_or_404(Post, category__name=category, pk=pk)
    return render(request, 'post/details.html', {'post': post})

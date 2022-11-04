from typing import List
from re import compile as re_compile
from urllib.parse import unquote
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from FreiRui.models.Categories import Categories
from FreiRui.models.Posts import Posts
from FreiRui.views.category.get_categories import get_categories

img_from_markdown = re_compile('!\[[^\]]*\]\((.*?)\s*(\"(?:.*[^\"])\")?\s*\)')


def post_details(request: HttpRequest, category: str, pk: str) -> HttpResponse:
    category = category.replace('_', ' ')
    category = unquote(category)
    categories = get_categories(request)
    post = get_object_or_404(Posts, category__name=category, pk=pk)
    previewImgLink = (img_from_markdown.search(post.text) or [None, None])[1]
    previewTitle = post.title
    previewDescription = post.text[:200]
    return render(request, 'post/details.html', {
        'post': post,
        'categories': categories,
        'previewImgLink': previewImgLink,
        'previewTitle': previewTitle,
        'previewDescription': previewDescription
    })

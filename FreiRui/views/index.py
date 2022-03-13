from typing import List
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse

from FreiRui.models.Categories import Categories
from FreiRui.views.post.list import post_list
from FreiRui.views.category.new import category_new


def index(request: HttpRequest) -> HttpResponse:
    categories: List[Categories] = Categories.objects.filter(
        published=True, ).order_by('order')
    if len(categories) > 0:
        category = categories[0]
        posts_view = post_list(request, category.name)
        return posts_view
    # else:
    if request.user.is_authenticated:
        return category_new(request)
    # else:
    return redirect('/admin')

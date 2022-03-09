from typing import List
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from FreiRui.models.Category import Category
from FreiRui.models.Gallery import Gallery
from FreiRui.models.Images import Images
from FreiRui.models.Post import Post


@login_required
def gallery_list(request: HttpRequest) -> HttpResponse:
    if (request.user.is_authenticated):
        categories: List[Category] = Category.objects.order_by('order')
        posts: List[Post] = Post.objects.order_by('published_date')
    else:
        posts: List[Post] = Post.objects.filter(
        category__published=True).order_by('published_date')
        categories: List[Category] = Category.objects.filter(published=True, ).order_by('order')
    posts_list = [*posts]
    galleries: List[List[str]] = []

    for post in posts_list:
        all_galeries: List[Gallery] = [*post.galleries.all()]
        pictures_in_post: List[str] = []
        for gallery in all_galeries:
            Images.objects.filter(gallery=gallery)
            all_images: List[Images] = Images.objects.filter(gallery=gallery)
            images_links: List[str] = [str(image.image)
                                       for image in all_images]
            pictures_in_post = [*pictures_in_post, *images_links]
        galleries.append(pictures_in_post)
    return render(request, 'gallery/list.html', {'galleries': galleries, 'categories': categories})

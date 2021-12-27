from django.shortcuts import render, get_object_or_404
from FreiRui.models.Post import Post


def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/details.html', {'post': post})

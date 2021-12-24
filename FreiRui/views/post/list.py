from django.shortcuts import render
from django.utils import timezone
from ...models.Post import Post


def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post/list.html', {'posts': posts})

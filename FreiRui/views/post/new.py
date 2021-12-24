
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, redirect

from ...admin.post_forms import PostForm


@login_required
def post_new(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        post_form = PostForm()
    return render(request, 'post/edit.html', {'post_form': post_form})

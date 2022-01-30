
from typing import Union
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, redirect

from FreiRui.admin.post_forms import PostForm

ResponseOrRedirect = Union[HttpResponse,
                           HttpResponseRedirect, HttpResponsePermanentRedirect]


@login_required
def post_new(request: HttpRequest) -> ResponseOrRedirect:
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

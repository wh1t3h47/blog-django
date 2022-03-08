
from typing import Union
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render

from FreiRui.admin.post_forms import PostForm
from .forms import return_rendered_html_forms

ResponseOrRedirect = Union[HttpResponse,
                           HttpResponseRedirect, HttpResponsePermanentRedirect]


@login_required
def post_new(request: HttpRequest) -> ResponseOrRedirect:
    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post: PostForm = post_form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            post_form.save_m2m()
            return HttpResponseRedirect(f"/posts/{post_form.cleaned_data['category']}/{post.pk}")
    # else if request.method == "GET":
    post_form = PostForm()
    return return_rendered_html_forms(request, post_form)

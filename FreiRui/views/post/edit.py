from typing import Union
from django import forms
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from FreiRui.models.Images import Images
from FreiRui.admin.post_forms import PostForm
from FreiRui.admin.image_forms import ImageForm
from FreiRui.models.Post import Post
from FreiRui.views.post.forms import return_rendered_html_forms
from .forms import return_rendered_html_forms

ResponseOrRedirect = Union[HttpResponseRedirect, HttpResponse]


@login_required
def post_edit(request: HttpRequest, pk: str) -> ResponseOrRedirect:
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            saved_post_form: PostForm = post_form.save(commit=False)
            saved_post_form.user = request.user
            saved_post_form.update_date = timezone.now()
            saved_post_form.save()
            post_form.save_m2m()
            # O usuário teria que ser administrador para conseguir redirecionar
            # e redirecionaria internamente apenas, não open redirection
            # deepcode ignore OR: <>
            return HttpResponseRedirect(f"/{post_form.cleaned_data['category']}/{pk}")
        else:
            print(post_form.errors)
    # print(f'formset: {formset}')
        return return_rendered_html_forms(request, post_form, pk)

    # else if request.method == "GET":
    post_form = PostForm()
    return return_rendered_html_forms(request, post_form, pk)

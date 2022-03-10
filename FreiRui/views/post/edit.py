from typing import Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from FreiRui.admin.post_forms import PostForm
from FreiRui.models.Posts import Posts
from FreiRui.views.post.forms import return_rendered_html_forms
from .forms import return_rendered_html_forms

ResponseOrRedirect = Union[HttpResponseRedirect, HttpResponse]


@login_required
def post_edit(request: HttpRequest, pk: str) -> ResponseOrRedirect:
    if request.method == "POST":
        post = get_object_or_404(Posts, pk=pk)
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            saved_post_form: PostForm = post_form.save(commit=False)
            saved_post_form.user = request.user
            saved_post_form.update_date = timezone.now()
            saved_post_form.save()
            post_form.save_m2m()
            # O usuário teria que ser administrador para conseguir redirecionar
            # e redirecionaria internamente apenas, não open redirection
            # deepcode ignore OR: <Motivo acima>
            return HttpResponseRedirect(f"/posts/{post_form.cleaned_data['category']}/{pk}")
        else:
            print(post_form.errors)
            messages.error(request, "Post not updated")
    # print(f'formset: {formset}')
        return return_rendered_html_forms(request, post_form, pk)

    # else if request.method == "GET":
    post_form = PostForm()
    response = return_rendered_html_forms(request, post_form, pk)
    response['Cache-Control'] = f'max-age={-1}'
    return response

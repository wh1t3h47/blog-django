from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from FreiRui.models.Images import Images
from FreiRui.admin.post_forms import PostForm
from FreiRui.admin.image_forms import ImageForm
from FreiRui.models.Post import Post


@login_required
def post_edit(request, pk):
    if request.method == "POST":
        post = get_object_or_404(Post, pk=pk)
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form = post_form.save(commit=False)
            post_form.user = request.user
            post_form.pubblished_date = timezone.now()
            post_form.save()
            return HttpResponseRedirect(f"/post/{pk}")
        else:
            print(post_form.errors)
    # print(f'formset: {formset}')
        return render(request, 'post/edit.html',
                      {'post_form': post_form})

    # else if request.method == "GET":
    post_form = PostForm()
    # print(f'formset: {formset}')
    return render(request, 'post/edit.html',
                  {'post_form': post_form})

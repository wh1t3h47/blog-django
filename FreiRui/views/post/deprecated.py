from django.shortcuts import get_object_or_404, render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils import timezone

from FreiRui.models.Posts import Posts
from ...admin.image_forms import ImageForm
from ...admin.post_forms import PostForm
from ...models.Images import Images

# ESSE ARQUIVO NÃO ESTA SENDO USADO

image_form_set = modelformset_factory(Images,
                                      form=ImageForm, extra=30)
# 'extra' means the number of photos that you can upload  ^


@login_required
def post_image_upload(request, pk: str):
    post = get_object_or_404(Posts, pk=pk)
    post_form = PostForm(request.POST, instance=post)
    formset = image_form_set(request.POST, request.FILES,
                             queryset=Images.objects.none())

    if post_form.is_valid() and formset.is_valid():
        post_form = post_form.save(commit=False)
        post_form.user = request.user
        post_form.published_date = timezone.now()
        post_form.save()

        for form in formset.cleaned_data:
            # this helps to not crash if the user
            # do not upload all the photos
            if form:
                image = form['image']
                photo = Images(post=post_form, image=image)
                photo.save()
        # use django messages framework
        messages.success(request,
                         "Uploaded image to post")
        return HttpResponseRedirect(f"/post/{pk}")
    else:
        print(post_form.errors, formset.errors)
        messages.error(request, "Image not uploaded")
        messages.error(request, str(post_form.errors))
    # print(f'formset: {formset}')
    return render(request, 'post/edit.html',
                  {'post_form': post_form, 'formset': formset})


@login_required
def get_image_upload(request):
    post_form = PostForm()
    formset = image_form_set(queryset=Images.objects.none())
    # print(f'formset: {formset}')
    return render(request, 'post/edit.html',
                  {'post_form': post_form, 'formset': formset})

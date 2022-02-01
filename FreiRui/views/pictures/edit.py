import json
from typing import Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from FreiRui.admin.image_forms import ImageForm
from FreiRui.models.Gallery import Gallery
from FreiRui.models.Images import Images

ResponseOrRedirect = Union[HttpResponse, HttpResponseRedirect]


@login_required
def image_edit(request: HttpRequest, picture_path: str) -> ResponseOrRedirect:
    if request.method == "POST":
        print('post')
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            print('valid')
            image = request.FILES.get('images')
            print(picture_path)
            if image and image.size > 0:
                print('image')
                picture = get_object_or_404(Images, image=picture_path)
                print(f"picture path: {picture.image.url}, request path: {picture_path}")
                gallery: Gallery = picture.gallery
                picture.image.delete()
                picture.image = image
                # sinaliza para o modelo não gerar um novo nome para a imagem
                picture.edit_image = True
                picture.image_url = picture_path
                # picture.image.url = picture_path
                picture.save()

                messages.success(request, "Image updated")

                return HttpResponseRedirect(picture.image.url)
        else:
            print(image_form.errors)
    # else if request.method == "GET":
    image_form = ImageForm()
    # disallow multiple files
    image_form.fields['images'].widget.attrs['multiple'] = False
    picture = get_object_or_404(Images, image=picture_path)
    # print(f'formset: {formset}')
    return render(request, 'picture/edit.html', {'image_form': image_form, 'picture': picture})

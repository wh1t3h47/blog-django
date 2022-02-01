import json
from typing import Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from FreiRui.admin.edit_image_forms import EditImageForm
from FreiRui.models.Gallery import Gallery
from FreiRui.models.Images import Images

Response = Union[HttpResponse, JsonResponse]


@login_required
def image_edit(request: HttpRequest, picture_path: str) -> Response:
    if request.method == "POST":
        print('post')
        image_form = EditImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            print('valid')
            image = request.FILES.get('images')
            print(picture_path)
            if image and image.size > 0:
                print('image')
                picture = get_object_or_404(Images, image=picture_path)
                print(
                    f"picture path: {picture.image.url}, request path: {picture_path}")
                gallery: Gallery = picture.gallery
                picture.image.delete()
                picture.image = image
                # sinaliza para o modelo não gerar um novo nome para a imagem
                picture.edit_image = True
                picture.image_url = picture_path
                # picture.image.url = picture_path
                picture.save()

                messages.success(request, "Image updated")

                return JsonResponse({'image': picture.image.url}, status=201)
        else:
            print(image_form.errors)
    # else if request.method == "GET":
    image_form = EditImageForm()
    # disallow multiple files
    image_form.fields['images'].widget.attrs['multiple'] = False
    # hide form
    image_form.fields['images'].widget.attrs['style'] = "display: none;"
    picture = get_object_or_404(Images, image=picture_path)
    # print(f'formset: {formset}')
    return render(request, 'picture/edit.html', {'image_form': image_form, 'picture': picture})

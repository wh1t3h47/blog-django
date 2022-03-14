import json
from turtle import pu
from typing import List, Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from FreiRui.admin.edit_image_forms import EditImageForm
from FreiRui.models.Categories import Categories
from FreiRui.models.Galleries import Galleries
from FreiRui.models.Images import Images

Response = Union[HttpResponse, JsonResponse]


@login_required
def image_edit(request: HttpRequest, picture_path: str) -> Response:
    if request.method == "POST":
        image_form = EditImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            image = request.FILES.get('images')
            if image and image.size > 0:
                picture = get_object_or_404(Images, image=picture_path)
                gallery: Galleries = picture.gallery
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
            messages.error(request, "Image not updated")
            messages.error(request, str(image_form.errors))
    # else if request.method == "GET":
    image_form = EditImageForm()
    # disallow multiple files
    image_form.fields['images'].widget.attrs['multiple'] = False
    # hide form
    image_form.fields['images'].widget.attrs['style'] = "display: none;"
    picture = get_object_or_404(Images, image=picture_path)
    # print(f'formset: {formset}')
    if (request.user.is_authenticated):
        categories: List[Categories] = Categories.objects.order_by('order')
    else:
        categories: List[Categories] = Categories.objects.filter(
            published=True, ).order_by('order')
    return render(request, 'picture/edit.html', {'image_form': image_form, 'picture': picture, 'categories': categories})

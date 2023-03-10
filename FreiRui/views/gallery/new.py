from typing import List, Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from FreiRui.admin.image_forms import ImageForm
from FreiRui.models.Categories import Categories
from FreiRui.models.Images import Images
from FreiRui.models.Galleries import Galleries
from FreiRui.views.category.get_categories import get_categories

ResponseOrRedirect = Union[HttpResponse, JsonResponse]


@login_required
def gallery_new(request: HttpRequest) -> ResponseOrRedirect:
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('images')
            if images and len(images) > 0:
                images_urls: list[str] = list()
                gallery = Galleries()
                gallery.save()
                # now upload all the images to the gallery
                for image in images:
                    if image and image.size > 0:
                        photo = Images(image=image, gallery=gallery)
                        photo.save()
                        images_urls.append(photo.image.url)
                # use django messages framework
                messages.success(request,
                                 "Uploaded images to gallery")
                return JsonResponse({'images': images_urls, 'gallery_id': gallery.pk}, status=201)

        # will reach here if images are invalid
        # 422 = Unprocessable Entity
        return HttpResponse(status=422)
    # else if request.method == "GET":
    form = ImageForm()
    categories = get_categories(request)
    return render(request, 'gallery/new.html', {'form': form, 'categories': categories})

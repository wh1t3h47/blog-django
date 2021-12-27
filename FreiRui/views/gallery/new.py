from django.http.response import HttpResponse
from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from FreiRui.admin.image_forms import ImageForm
from FreiRui.models.Images import Images
from FreiRui.models.Gallery import Gallery

image_form_set = modelformset_factory(Images,
                                      form=ImageForm, extra=30)
# 'extra' means the number of photos that you can upload  ^


@login_required
def gallery_new(request):
    if request.method == "POST":
        formset = image_form_set(request.POST, request.FILES,
                                 queryset=Images.objects.none())
        if formset.is_valid():
            gallery = Gallery()
            # to get a PK for the gallery
            gallery.save(commit=False)
            for form in formset.cleaned_data:
                # this helps to not crash if the user
                # do not upload all the photos
                if form:
                    image = form['image']
                    photo = Images(image=image, gallery=gallery)
                    photo.save()
            gallery.save()
            # use django messages framework
            messages.success(request,
                             "Uploaded image to gallery")
            return HttpResponse(status=201)
        else:
            print(formset.errors)
        # print(f'formset: {formset}')
        # 422 = Unprocessable Entity
        return HttpResponse(status=422)
    # else if request.method == "GET":
    formset = image_form_set(queryset=Images.objects.none())
    # print(f'formset: {formset}')
    return render(request, 'post/edit.html',
                  {'formset': formset})

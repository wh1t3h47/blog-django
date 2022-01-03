
from typing import Union
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, redirect

from FreiRui.admin.category_forms import CategoryForm

ResponseOrRedirect = Union[HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect]

@login_required
def category_new(request: HttpRequest) -> ResponseOrRedirect:
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category_edit', pk=category_form.instance.pk)
    else:
        category_form = CategoryForm()
        # Default value, this is not set in the model because it interferes
        # with the edit page and overwrites the actual published value.
        category_form.fields['published'].widget.attrs['checked'] = True
    return render(request, 'category/edit.html', {'category_form': category_form})


from typing import List, Union
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect

from FreiRui.admin.category_forms import CategoryForm
from FreiRui.models.Category import Category

ResponseOrRedirect = Union[HttpResponse,
                           HttpResponseRedirect, HttpResponsePermanentRedirect]


@login_required
def category_new(request: HttpRequest) -> ResponseOrRedirect:
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('category_edit', pk=category_form.instance.pk)
    category_form = CategoryForm()
    # Default value, this is not set in the model because it interferes
    # with the edit page and overwrites the actual published value.
    category_form.fields['published'].widget.attrs['checked'] = True
    category_form.fields['listing_type'].widget.attrs['style'] = 'display: none;'
    categories: List[Category] = Category.objects.filter(published=True, ).order_by('order')
    return render(request, 'category/edit.html', {'category_form': category_form, 'categories': categories})

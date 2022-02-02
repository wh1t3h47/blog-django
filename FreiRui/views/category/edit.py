from typing import List, Union
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required

from FreiRui.admin.category_forms import CategoryForm
from FreiRui.models.Category import Category

ResponseOrRedirect = Union[HttpResponse, HttpResponseRedirect]


@login_required
def category_edit(request: HttpRequest, pk: str) -> ResponseOrRedirect:
    if request.method == "POST":
        category = get_object_or_404(Category, pk=pk)
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            return HttpResponseRedirect(f"/category/{pk}/edit")
        else:
            print(category_form.errors)
    # print(f'formset: {formset}')
        return render(request, 'category/edit.html',
                      {'category_form': category_form, 'category': category})

    # else if request.method == "GET":
    category_form = CategoryForm()
    category = get_object_or_404(Category, pk=pk)
    category_form.fields['name'].widget.attrs['value'] = category.name
    category_form.fields['published'].widget.attrs['checked'] = category.published
    category_form.fields['listing_type'].widget.attrs['style'] = 'display: none;'
    # print(f'formset: {formset}')
    categories: List[Category] = Category.objects.filter(published=True, ).order_by('order')
    return render(request, 'category/edit.html',
                  {'category_form': category_form, 'category': category, 'categories': categories})

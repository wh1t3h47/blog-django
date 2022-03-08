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
        previous_name = category.name
        category_form = CategoryForm(request.POST, instance=category)
        if category_form.is_valid():
            category: Category = category_form.save(commit=False)
            category.name = str.replace(category.name, '/', '')
            category.name = str.replace(category.name, '_', '')
            categories_matching_name = Category.objects.filter(name=category.name).count()
            if categories_matching_name > 0 and category.name != previous_name:
                messages.error(request, 'Category name already exists')
                if (request.user.is_authenticated):
                    categories: List[Category] = Category.objects.order_by('order')
                else:
                    categories: List[Category] = Category.objects.filter(published=True, ).order_by('order')
                return render(request, 'category/edit.html', {'category_form': category_form, 'category': category, 'categories': categories, 'failed_category_exists': True})
            category.save()
            return HttpResponseRedirect(f"/category/{pk}/edit")
        else:
            print(category_form.errors)
    # print(f'formset: {formset}')
        return render(request, 'category/edit.html',
                      {'category_form': category_form, 'category': category})

    # else if request.method == "GET":
    category_form = CategoryForm()
    category = get_object_or_404(Category, pk=pk)
    # category_form.fields['name'].widget.attrs['value'] = category.name
    # category_form.fields['published'].widget.attrs['checked'] = category.published
    # category_form.fields['listing_type'].widget.attrs['style'] = 'display: none;'
    # category_form.fields['order'].widget.attrs['value'] = category.order
    # category_form.fields['short_name'].widget.attrs['value'] = category.short_name
    # category_form.fields['title'].widget.attrs['value'] = category.title
    # print(f'formset: {formset}')
    if (request.user.is_authenticated):
        categories: List[Category] = Category.objects.order_by('order')
    else:
        categories: List[Category] = Category.objects.filter(published=True, ).order_by('order')
    return render(request, 'category/edit.html',
                  {'category_form': category_form, 'category': category, 'categories': categories})

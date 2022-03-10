
from typing import List, Union
from django.contrib.auth.decorators import login_required
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages

from FreiRui.admin.category_forms import CategoryForm
from FreiRui.models.Categories import Categories

ResponseOrRedirect = Union[HttpResponse,
                           HttpResponseRedirect, HttpResponsePermanentRedirect]


@login_required
def category_new(request: HttpRequest) -> ResponseOrRedirect:
    default_fields = {'order': 0, 'published': True}
    if request.method == "POST":
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            # save but dont commit
            category: Categories = category_form.save(commit=False)
            category.name = str.replace(category.name, '/', '')
            category.name = str.replace(category.name, '_', '')
            categories_matching_name = Categories.objects.filter(name=category.name).count()
            if categories_matching_name > 0:
                messages.error(request, 'Category name already exists')
                if (request.user.is_authenticated):
                    categories: List[Categories] = Categories.objects.order_by('order')
                else:
                    categories: List[Categories] = Categories.objects.filter(published=True, ).order_by('order')
                return render(request, 'category/edit.html', {'category_form': category_form, 'category': category, 'categories': categories, 'failed_category_exists': True})
            category.save()
            return redirect('post_list', category=category.name)
    category_form = CategoryForm()
    # Default value, this is not set in the model because it interferes
    # with the edit page and overwrites the actual published value.
    category_form.fields['published'].widget.attrs['checked'] = True
    category_form.fields['listing_type'].widget.attrs['style'] = 'display: none;'
    if (request.user.is_authenticated):
        categories: List[Categories] = Categories.objects.order_by('order')
    else:
        categories: List[Categories] = Categories.objects.filter(published=True, ).order_by('order')
    return render(request, 'category/edit.html', {'category_form': category_form, 'categories': categories, 'category': default_fields})

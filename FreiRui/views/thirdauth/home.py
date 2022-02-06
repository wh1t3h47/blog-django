from django.shortcuts import render
from django.template.context import RequestContext


def home(request):
    return render(request, 'thirdauth/home.html',
                  {'user': request.user})

# Translation middleware will check a cookie and set the language accordingly
from typing import Callable
from django.http import HttpRequest, HttpResponse
from django.utils.translation import activate


def translation_middleware(get_response: Callable[[HttpRequest], HttpResponse]):

    def middleware(request: HttpRequest):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        lang = request.COOKIES.get('lang') or 'pt'
        if lang:
            activate(lang)

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

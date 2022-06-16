# Translation middleware will check a cookie and set the language accordingly

from django.http import HttpRequest, HttpResponse
from django.utils.translation import activate


def translation_middleware(get_response: lambda HttpRequest: HttpResponse) -> HttpResponse:

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        lang = request.COOKIES.get('lang')
        if lang:
            activate(lang)

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from tarfile import open as tarfile_open


@login_required
def backup_media(request: HttpRequest):
    '''
    View para fazer backup da pasta media, essa view retorna um arquivo
    .tar.gz contendo tudo que tem na pasta media, esse arquivo vai ser
    baixado diretamente, sem um HTML.
    '''
    try:
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='application/x-tar')
        response['Content-Disposition'] = 'attachment; filename="media_backup.tar.gz"'
        # Create the tarfile object
        with tarfile_open(fileobj=response, mode="w:gz") as tar:
            # Add the media folder to the tarfile
            tar.add(settings.MEDIA_ROOT, arcname='media')
        # Return the response
        return response
    except Exception as e:
        messages.error(request, 'Error creating backup')
        messages.error(request, str(e))

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
# from tarfile import open as tarfile_open
from tarsafe import open as tarfile_open

def extract_inside_folder(tar, folder="media/"):
    after_folder = len(folder)
    for member in tar.getmembers():
        if member.path.startswith(folder):
            member.path = member.path[after_folder:]
            yield member


@login_required
def restore_media(request: HttpRequest): 
    '''
    View para fazer restauração de um arquivo .tar.gz, esse arquivo vai
    conter uma pasta media com os arquivos e vai ser enviado por post
    esse arquivo vai ser upado diretamente, por um form sem um template.
    '''
    if request.method == 'GET':
        # return method not supported
        return HttpResponseRedirect('/admin/')
    # else

    try:
        # Get the uploaded file
        uploaded_file = request.FILES['file']
        # Create the tarfile from the uploaded file
        with tarfile_open(fileobj=uploaded_file, mode='r:gz') as tar:
            # Extract anything from the tarfile's folder media to the media folder
            tar.extractall(path=settings.MEDIA_ROOT, members=extract_inside_folder(tar))
        # Return the response
        messages.success(request, 'Restored media')
        return HttpResponseRedirect('/admin/')
    except Exception as e:
        messages.error(request, 'Error restoring media')
        messages.error(request, str(e))
        return HttpResponseRedirect('/admin/')

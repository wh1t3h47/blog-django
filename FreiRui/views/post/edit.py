from django.contrib.auth.decorators import login_required
from .image_upload import get_image_upload, post_image_upload


@login_required
def post_edit(request, pk):
    if request.method == "POST":
        return post_image_upload(request, pk)
    # else:
    return get_image_upload(request)

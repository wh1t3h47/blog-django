from django.urls import path

from FreiRui.views.admin.backup_media import backup_media
from FreiRui.views.admin.restore_media import restore_media

urlpatterns = [
    path('backup_media/', backup_media, name='backup_media'),
    path('restore_media/', restore_media, name='restore_media'),
]

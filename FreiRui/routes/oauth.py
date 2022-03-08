from django.urls import include, path
from FreiRui.views.oauth.facebook_post import FacebookPost
from FreiRui.views.oauth.settings import Settings


urlpatterns = [
    path('oauth/', include('social_django.urls', namespace='social')),
    path('settings/', Settings.as_view(), name='settings'),
    path('post_to_facebook/', FacebookPost.as_view(), name='post_to_facebook'),
]

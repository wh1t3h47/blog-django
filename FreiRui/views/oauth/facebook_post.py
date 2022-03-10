from typing import List

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from social_django.models import UserSocialAuth

from FreiRui.models.Posts import Posts
from FreiRui.models.Images import Images

from facepy import GraphAPI
from bs4 import BeautifulSoup
from markdown import markdown

def get_images(galleries_id: List[str]):
    all_images: List[str] = []
    for gallery_id in galleries_id:
        images: List[Images] = Images.objects.filter(gallery_id=gallery_id)
        images = [str(img.image) for img in images]
        all_images = [*all_images, *images]
    return all_images

@method_decorator(csrf_exempt, name='dispatch')
class FacebookPost(LoginRequiredMixin, TemplateView):
    def _get_unpublished_facebook_posts(self) -> List[Posts]:
        posts: List[Posts] = Posts.objects.filter(
            category__published=True,
            is_deleted=False,
            published_date__lte=timezone.now(),
            # facebook_posted=False,
        )
        return posts

    # get returns self.post()
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.user

        try:
            github_login = user.social_auth.get(provider='github')
        except UserSocialAuth.DoesNotExist:
            github_login = None

        try:
            twitter_login = user.social_auth.get(provider='twitter')
        except UserSocialAuth.DoesNotExist:
            twitter_login = None

        try:
            facebook = user.social_auth.get(provider='facebook')
            facebook_oauth_token = facebook.extra_data['access_token']
            for id in dict.keys(facebook.__dict__):
                print(id)
            for id in dict.keys(facebook.extra_data):
                print(id)
            unpublished_posts = self._get_unpublished_facebook_posts()
            for post in unpublished_posts:
                graph = GraphAPI(facebook_oauth_token)
                html = markdown(post.text)
                plain_text = ''.join(BeautifulSoup(html, features="lxml").findAll(text=True))
                text = f"{post.title}\n{plain_text}"
                images = get_images(post.galleries.all())
                post = {
                    "caption": text,
                    "url": f"http://localhost/{images[0]}"
                }
                print(images)
                user_id = facebook.uid
                graph.post(path=f"{user_id}/photos", url=f"http://localhost/{images[0]}", published=False)
                # graph.post(path="me/photos", message=text, url=f"http://localhost/{images[0]}")

                post.facebook_posted = True
                # post.save()
        except UserSocialAuth.DoesNotExist:
            facebook = None

        # return json response with success
        return JsonResponse({"success": True}, status=201)

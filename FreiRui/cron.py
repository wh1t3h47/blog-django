from requests import post
import environ

env = environ.Env()
environ.Env.read_env()

def post_to_facebook():
    r = post(f"{env('HOST')}/post_to_facebook/")

def post_to_instagram():
    pass


def post_to_social_media():
    print('Posting to social media...')
    try:
        post_to_facebook()
    except:
        pass
    try:
        post_to_instagram()
    except:
        pass

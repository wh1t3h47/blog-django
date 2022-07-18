"""
Django settings for FreiRui project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from os.path import join

import environ

env = environ.Env()

environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')
DEBUG = True if (DEBUG in ['True', 'true', 'TRUE', '1']) else False

ALLOWED_HOSTS = [env('HOST')]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdownify.apps.MarkdownifyConfig',
    'social_django',
    'django_crontab',
    'request',
    'smuggler',
    'defender',
    'modeltranslation',
    'FreiRui',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'request.middleware.RequestMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
    'defender.middleware.FailedLoginMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'FreiRui.middleware.translation_middleware.translation_middleware',
]

ROOT_URLCONF = 'FreiRui.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'FreiRui.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'


def gettext(s): return s


LANGUAGES = [
    ('de', gettext('German')),
    ('en', gettext('English')),
    ('pt', gettext('Portuguese')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'pt'

MODELTRANSLATION_FALLBACK_LANGUAGES = {
    'en': ('pt', 'de'),
    'default': ('en', 'de'),
    'de': ('en', 'pt'),
}

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Image upload configuration

MEDIA_URL = '/media/'

# Path where media is stored
MEDIA_ROOT = join(BASE_DIR, 'media/')

# Social Auth configuration
AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

# LOGIN_URL = 'login'
# LOGOUT_URL = 'logout'
# LOGIN_REDIRECT_URL = 'home'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

SOCIAL_AUTH_FACEBOOK_KEY = env('FB_APP_ID')
SOCIAL_AUTH_FACEBOOK_SECRET = env('FB_APP_SECRET')

# Schedule social media posts
CRONJOBS = [
    ('*/2 * * * *', 'FreiRui.cron.post_to_social_media'),
]

REQUEST_BASE_URL = 'https://env("HOST")'
REQUEST_IGNORE_USER_AGENTS = (
    r'^$',  # ignore requests with no user agent string set
    r'Googlebot',
    r'Baiduspider',
)
REQUEST_PLUGINS = (
    'request.plugins.TrafficInformation',
    'request.plugins.LatestRequests',
    'request.plugins.TopPaths',
    'request.plugins.TopErrorPaths',
    'request.plugins.TopReferrers',
    'request.plugins.TopSearchPhrases',
    'request.plugins.TopBrowsers',
)
REQUEST_TRAFFIC_MODULES = (
    'request.traffic.UniqueVisitor',
    'request.traffic.UniqueVisit',
    'request.traffic.Hit',
    'request.traffic.Error',
)
REQUEST_VALID_METHOD_NAMES = (
    'get',
)
REQUEST_IGNORE_AJAX = True
# Não ignorar esse caminho, pois assim podemos logar tentativas de login
# REQUEST_IGNORE_PATHS = (
#     r'^admin/',
# )
REQUEST_IGNORE_USERNAME = 'admin'

MARKDOWNIFY = {
    "default": {
        "WHITELIST_TAGS": [
            'a',
            'abbr',
            'acronym',
            'b',
            'blockquote',
            'em',
            'i',
            'li',
            'ol',
            'p',
            'strong',
            'ul',
            'span',
            'img',
            'h1',
            'h2',
            'h3',
            'h4',
            'h5',
            'h6',
            'pre',
            'code',
            'table',
            'thead',
            'tbody',
            'th',
            'tr',
            'td',
            'br',
            'hr',
            'div',
            'sup',
            'sub',
            'blockquote',
            'strike',
            'strong',
        ],
        "WHITELIST_ATTRS": [
            'href',
            'src',
            'alt',
            'style'
        ],
        "WHITELIST_STYLES": [
            'color',
            'display',
            'text-align'
        ]
    }
}

REDIS_PASSWORD = env('REDIS_PASSWORD')
REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')
REDIS_URL = f"redis://:{REDIS_PASSWORD}@{REDIS_HOST}:{REDIS_PORT}"
DEFENDER_REDIS_URL = REDIS_URL

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'{REDIS_URL}/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient'
        },
        'KEY_PREFIX': 'django_orm'
    }
}

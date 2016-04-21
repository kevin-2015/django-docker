# -*- coding:utf-8 -*-
import os
from os.path import join, dirname

REDIS_CONN = os.environ.get('REDIS_CONN', 'redis://127.0.0.1:6379/2')
MYSQL_CONN = os.environ.get('MYSQL_CONN', None)
DEBUG = (os.environ.get('DEBUG', 'TRUE').upper() == 'TRUE')  # True by default


BASE_DIR = dirname(dirname(__file__))
ALLOWED_HOSTS = ['*']

if not MYSQL_CONN:  # use sqlite3
    # print '!!! no MYSQL_CONN found. using sqlite3'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:  # use mysql
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'django',
            'USER': 'root',
            'PASSWORD': 'Jackon123',
            'HOST': MYSQL_CONN,
            'PORT': '',
        }
    }


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_CONN,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}


# Internationalization

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'
DATE_FORMAT = 'Y-m-d'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '477)6e=2+$21qe8)@w#bq=f1anv5ebxf)g+*cv7=__lt^)5c30'

# Application definition

INSTALLED_APPS = (
    # 'grappelli',  # beautiful admin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # multi sites.
    'rest_framework',
    'django_filters',
    'accounts',
)

SITE_ID = 1  # required if contrib.sites is present

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'base.urls'

WSGI_APPLICATION = 'base.wsgi.application'


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'

STATIC_ROOT = join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    # join(BASE_DIR, 'base/static'),
)


# Template files

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # join(BASE_DIR, 'base/templates'),
            # join(BASE_DIR, 'accounts/templates'),  # load before userena
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                "django.core.context_processors.i18n",
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'base.context_processors.site_info',
            ],
        },
    },
]


# Media files

MEDIA_URL = '/media/'

MEDIA_ROOT = join(BASE_DIR, "media")


# Auth (login)

LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


try:
    from local_settings import *  # noqa
except Exception as e:
    pass

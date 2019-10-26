"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '$to#b+iqo3@0yk$6%7c9pf$b=$jnmz93fbtktmyxa(nbso^o2m'

ALLOWED_HOSTS = ['*.*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cacheops',
    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework_jwt',
    'versatileimagefield',

    'app.authorization',
    'app.product',
    'app.coupon',
    'app.order',
    'app.source',
    'app.notice',
    'app.payment',
    'app.booking',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'middleware.jwt_auth.JWTAuthenticationMiddleware',
]

REST_FRAMEWORK = {
    'ORDERING_PARAM': 'sorter',
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',

        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    ),
    'DEFAULT_PAGINATION_CLASS': 'middleware.rest_framework.CustomPagination',
    'EXCEPTION_HANDLER': 'middleware.utils.custom_exception_handler'
}

ROOT_URLCONF = 'backend.urls'
AUTH_USER_MODEL = 'authorization.CustomUser'
WSGI_APPLICATION = 'backend.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Dubai'

USE_I18N = True

USE_L10N = False

USE_TZ = True

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'static')

MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
MEDIA_ROOT = os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)), 'media')


#缓存
CACHEOPS_DEFAULTS = {
    'timeout': 60*60
}

CACHEOPS = {
    'auth.user': {'ops': 'get', 'timeout': 60*15},
    'auth.*': {'ops': ('fetch', 'get')},
    'auth.permission': {'ops': 'all'},
    '*.*': {},
}

# 跨域
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:8080', 'http://localhost:8080', 'ugodubai.com']
CORS_ALLOW_HEADERS = ('*',)
CORS_ALLOW_METHODS = ('*',)

# 图片压缩
VERSATILEIMAGEFIELD_RENDITION_KEY_SETS = {
    'product_size': [
        ('full_size', 'url'),
        ('thumbnail', 'thumbnail__100x100'),
        ('large_square_crop', 'crop__400x400'),
        ('small_square_crop', 'crop__50x50'),
        ('medium_square_crop', 'crop__200x200'),
        ('gallery_square_crop', 'crop__524x288'),
    ]
}
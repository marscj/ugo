from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['ugodubai.com', '*']

# SESSION_COOKIE_DOMAIN = 'ugodubai.com'

CORS_ORIGIN_ALLOW_ALL = False

# CACHEOPS_REDIS = "redis://127.0.0.1:6379/0"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ugo',
        'USER': 'admin',
        'PASSWORD': 'admin123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_AUTH_COOKIE': 'Access-Token',
}
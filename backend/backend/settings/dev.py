from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['ugodubai.com', '*']

# SESSION_COOKIE_DOMAIN = 'ugodubai.com'

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
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'postgres',
    #     'USER': 'postgres',
    #     'PASSWORD': 'password123',
    #     'HOST': '47.52.175.23',
    #     'PORT': '5433',
    # },
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1), 
    'JWT_AUTH_COOKIE': 'Access-Token',
}
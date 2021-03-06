from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['ugodubai.com', '*']

# SESSION_COOKIE_DOMAIN = 'ugodubai.com'

CORS_ORIGIN_ALLOW_ALL = True

# CACHEOPS_REDIS = "redis://redis:6379/0"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password123',
        'HOST': '47.52.175.23',
        'PORT': '5432',
    },
    'slave': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'password123',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# DATABASE_ROUTERS = ['middleware.router.Router',]

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
    'JWT_AUTH_COOKIE': 'Access-Token',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': None,
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    },
}
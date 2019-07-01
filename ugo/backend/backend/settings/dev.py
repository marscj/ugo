from .settings import *

DEBUG = True

ALLOWED_HOSTS = ['*']

SESSION_COOKIE_DOMAIN = 'ugonew.com'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ugo',
#         'USER': 'admin',
#         'PASSWORD': 'admin123',
#         'HOST': 'localhost',
#         'PORT': 5432,
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300), 
    'JWT_AUTH_COOKIE': 'jwt_auth_token',
    'JWT_GET_USER_SECRET_KEY': 'ubang.user.models.jwt_get_secret_key'
}
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'chat',
        'USER': 'chat_admin',
        'PASSWORD': 'chat_admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


STATIC_DIR = os.path.join(BASE_DIR, 'static'),
STATICFILES = [STATIC_DIR, ]
STATIC_URL = '/static/'

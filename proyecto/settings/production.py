from .base import *
import os

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DEBUG = True

ALLOWED_HOSTS = ['parauco.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'crud_django',
        'USER': 'gonza',
        'PASSWORD': 'gonza30',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

#STATICFILES_DIRS = (BASE_DIR,'static'),
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = (os.path.join('C:\Django\Diseño','static'),)

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfiles/'),)

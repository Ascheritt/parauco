from .base import *
import os

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DEBUG = True

ALLOWED_HOSTS = ['parauco.herokuapp.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd2mi15rheeiqe5',
        'USER': 'mxvnxbvvvgsmzy',
        'PASSWORD': '98a2706fe9a00a6201bbfb0b5d52a678ae51d213f93d2e026723a64d7bef08d7',
        'HOST': 'ec2-50-19-221-38.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

#STATICFILES_DIRS = (BASE_DIR,'static'),
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = (os.path.join('C:\Django\Diseño','static'),)

STATIC_URL = '/static/'

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'staticfiles/'),)

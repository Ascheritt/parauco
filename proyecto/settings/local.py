from .base import *
import os

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DEBUG = True

ALLOWED_HOSTS = []

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        }
    },
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'proyecto1',
        'USER': 'gonza',
        'PASSWORD': 'gonza30',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join('C:\Django\AraucoP\indicador','static'),
)

STATIC_URL = '/static/'

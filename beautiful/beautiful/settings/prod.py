from .common import *


DEBUG = False
ALLOWED_HOSTS = ['18.188.35.118', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'NAME': 'beautiful',
        'USER': 'jubin3424',
        'PASSWORD': 'wnqls6013',
    },
}


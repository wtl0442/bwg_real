"""
Django settings for beautiful project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '50rds_cbh+uld9#^7(m851bft5^iq90a(q=!p_(gnqkpyr)^t('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static")
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'post',
    'accounts',
    'creator',
    'review',
    'event',

    'social_django',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.naver',

    'django_google_maps',
    'beautywiki',
    'django_summernote',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'beautiful.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'beautiful', 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'beautiful.context_processors.brand',
                'beautiful.context_processors.skintype',
                'beautiful.context_processors.category',
            ],
        },
    },
]



WSGI_APPLICATION = 'beautiful.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'bwg_db',
        # 'USER': 'jubin3424',
        # 'PASSWORD': 'wnqls6013',
        # 'HOST': '',
        # 'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'         #static관련 세팅들
STATIC_ROOT = 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'main', 'static'),
    os.path.join(BASE_DIR, 'review', 'static'),
    os.path.join(BASE_DIR, 'event', 'static'),
    ]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media'

LOGIN_URL = '/accounts/login/'
LOGOUT_URL = '/accounts/logout'
LOGIN_REDIRECT_URL = '/'

MAIN_REDIRECT_URL = '/'


AUTHENTICATION_BACKENDS = (
    'allauth.account.auth_backends.AuthenticationBackend',
    'django.contrib.auth.backends.ModelBackend',

    # 'social_core.backends.facebook.FacebookOAuth2',  # 페이스북
    # 'social_core.backends.kakao.KakaoOAuth2',  # 카카오톡
    # 'social_core.backends.naver.NaverOAuth2',  # 네이버


)

SOCIALACCOUNT_PROVIDERS = {
    'facebook': {
        'METHOD': 'oauth2',
        'SCOPE': ['email', 'public_profile', 'user_friends'],
        'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
        'INIT_PARAMS': {'cookie': True},
        'FIELDS': [
            'id',
            'email',
            'name',
            'first_name',
            'last_name',
            'verified',
            'locale',
            'timezone',
            'link',
            'gender',
            'updated_time',
        ],
        'EXCHANGE_TOKEN': True,
        'LOCALE_FUNC': lambda request: 'kr_KR',
        'VERIFIED_EMAIL': False,
        'VERSION': 'v2.4',
    }
}
SITE_ID = 1

SOCIALACCOUNT_AUTO_SIGNUP = False
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQURIED = True


SOCIAL_AUTH_FACEBOOK_KEY = '142505123102413'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET ='4ef1c71e6241ceb229763626d6dd820c'


# SOCIAL_AUTH_LOGIN_ERROR_URL = 'accounts/settings/'
# SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
# SOCIAL_AUTH_RAISE_EXCEPTIONS = False

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'wtl0442@gmail.com'
EMAIL_HOST_PASSWORD = 'tjfwhrud!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

GOOGLE_MAPS_API_KEY = 'AIzaSyCwJMUjrQFsJ4kO6d05KnQLRE3TAaxLv20'

SUMMERNOTE_CONFIG = {

    # Change editor size
    'width': '100%',
    'height': '480',
}

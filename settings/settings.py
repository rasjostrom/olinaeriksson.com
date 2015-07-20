"""
Django settings for settings project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&5&8@@i*h_*0e$yo4ooktxr7$!8f-vmhg+4i)fb366kt8pq70i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'tinymce',
    'gallery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'settings.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


# CAHNGE THIS TO A PRODUCTION READY DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/www/media/'

TINYMCE_JS_URL = '/static/tiny_mce/tiny_mce.js'
TINYMCE_JS_ROOT = '/var/www/static/tiny_mce/'

TINYMCE_COMPRESSOR = True

TINYMCE_DEFAULT_CONFIG = {
    'mode': 'textareas',
    'theme': "advanced",
    'plugins': 'paste, searchreplace, media, emotions',
    'theme_advanced_toolbar_align' : 'left',
    'theme_advanced_toolbar_location': 'top',
    'theme_advanced_buttons1':"bold,italic,underline,strikethrough,sub,sup,separator,justifyleft,justifycenter,justifyright,justifyfull,separator,formatselect,fontselect,fontsizeselect",
    'theme_advanced_buttons2':"bullist,numlist,outdent,indent,ltr,rtl,separator,link,unlink,anchor,image,separator,table,insertdate,inserttime,advhr,emotions,media,charmap,separator,undo,redo",
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 10,
}


from settings import *

DEBUG = True


# DEVELOPMENT DATABASE SETTINGS
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


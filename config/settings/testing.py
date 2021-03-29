from .base import *
from decouple import Csv


DEBUG = config('DEBUG', True)
ALLOWED_HOSTS = ['*']


# Environment
ENVIRONMENT = 'TESTING'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# SQLite
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Paypal
PAYPAL_RECEIVER_EMAIL = 'eyobofficial-facilitator@gmail.com'
PAYPAL_TEST = True


# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'mediafiles')


# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}

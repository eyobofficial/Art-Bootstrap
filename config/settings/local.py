from .base import *


DEBUG = config('DEBUG', True)
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_extensions',
]


# Environment
ENVIRONMENT = 'LOCAL'


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


# Caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

from .base import *


DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_extensions',
]


# Environment
ENVIRONMENT = 'LOCAL'


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

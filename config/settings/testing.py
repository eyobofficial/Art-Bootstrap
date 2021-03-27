from .base import *
from decouple import Csv


DEBUG = True
ALLOWED_HOSTS = ['*']


# Environment
ENVIRONMENT = 'TESTING'


# Paypal
PAYPAL_RECEIVER_EMAIL = 'eyobofficial-facilitator@gmail.com'
PAYPAL_TEST = True


# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}

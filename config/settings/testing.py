from .base import *
from decouple import Csv


DEBUG = True
ALLOWED_HOSTS = ['*']


# Hostname
HOSTNAME = 'http://testing.artbootstrap.com'


# Environment
ENVIRONMENT = 'TESTING'


# Paypal
PAYPAL_RECEIVER_EMAIL = 'eyobofficial-facilitator@gmail.com'
PAYPAL_TEST = True


# Cacheing
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache'
    }
}

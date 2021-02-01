from .base import *


DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'django_extensions',
]


# Paypal
PAYPAL_RECEIVER_EMAIL = 'eyobofficial-facilitator@gmail.com'
PAYPAL_TEST = True

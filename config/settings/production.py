from .base import *


DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Paypal
PAYPAL_RECEIVER_EMAIL = 'eyobofficial@gmail.com'
PAYPAL_TEST = False

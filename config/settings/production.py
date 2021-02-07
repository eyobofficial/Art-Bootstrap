from .base import *


DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Hostname
HOSTNAME = 'https://artbootstrap.com'


# Paypal
PAYPAL_RECEIVER_EMAIL = 'eyobofficial@gmail.com'
PAYPAL_TEST = False

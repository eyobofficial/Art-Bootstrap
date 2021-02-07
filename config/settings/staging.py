from .base import *
from decouple import config, Csv


DEBUG = False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Hostname
HOSTNAME = 'http://staging.artbootstrap.com'


# Paypal
PAYPAL_RECEIVER_EMAIL = 'eyobofficial-facilitator@gmail.com'
PAYPAL_TEST = True

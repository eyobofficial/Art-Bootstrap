from .base import *


DEBUG = config('DEBUG', False)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Environment
ENVIRONMENT = 'PRODUCTION'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# Postgresql
if len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if config('DATABASE_URL', None) is None:
        raise Exception('DATABASE_URL environment variable not defined')
    DATABASES = {
        'default': dj_database_url.parse(config('DATABASE_URL')),
    }


# Paypal
PAYPAL_RECEIVER_EMAIL = 'eyobofficial@gmail.com'
PAYPAL_TEST = False


# AWS S3
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_DEFAULT_ACL = None
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}


# Media files
MEDIA_LOCATION = 'mediafiles'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
DEFAULT_FILE_STORAGE = 'config.storage_backends.S3MediaStorage'


# Caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}


# django-compressor
COMPRESS_URL = STATIC_URL
COMPRESS_ROOT = os.path.join(BASE_DIR, 'staticfiles')

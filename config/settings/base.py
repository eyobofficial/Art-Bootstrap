import os
from decouple import config
from environ import Path

from django.core.management.utils import get_random_secret_key


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__) - 3


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY', get_random_secret_key())


# Application definition
INSTALLED_APPS = [
    'clearcache',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]


# Third Party apps
INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'phonenumber_field',
    'taggit',
    'paypal.standard.ipn',
    'django_social_share',
    'storages',
    'compressor',
    'robots',
    'django_browser_reload',
]


# Project apps
INSTALLED_APPS += [
    'accounts.apps.AccountsConfig',
    'shared.apps.SharedConfig',
    'themes.apps.ThemesConfig',
    'wishlist.apps.WishlistConfig',
    'cart.apps.CartConfig',
    'checkout.apps.CheckoutConfig',
    'contact.apps.ContactConfig',
    'about.apps.AboutConfig',
    'policy.apps.PolicyConfig',
    'affiliates.apps.AffiliatesConfig',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_browser_reload.middleware.BrowserReloadMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database (PostgreSQL)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('RDS_DB_NAME'),
        'USER': config('RDS_USERNAME'),
        'PASSWORD': config('RDS_PASSWORD'),
        'HOST': config('RDS_HOSTNAME'),
        'PORT': config('RDS_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Addis_Ababa'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Sites
SITE_ID = 1


# Custom Auth User Model
AUTH_USER_MODEL = 'accounts.CustomUser'


# Cors Headers
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SAMESITE = 'None'
SESSION_COOKIE_SAMESITE = 'None'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)


# django-compress
COMPRESS_ENABLED = True
COMPRESS_CSS_HASHING_METHOD = 'content'
COMPRESS_FILTERS = {
    'css':[
        'compressor.filters.css_default.CssAbsoluteFilter',
        'compressor.filters.cssmin.rCSSMinFilter',
    ],
    'js':[
        'compressor.filters.jsmin.JSMinFilter',
    ]
}
HTML_MINIFY = True
KEEP_COMMENTS_ON_MINIFYING = True


# Default Admin Account
DEFAULT_ADMIN_EMAIL = config('ADMIN_EMAIL')
DEFAULT_ADMIN_PASSWORD = config('ADMIN_PASSWORD')
DEFAULT_ADMIN_FIRST_NAME = config('ADMIN_FIRST_NAME', '')
DEFAULT_ADMIN_LAST_NAME = config('ADMIN_LAST_NAME', '')


# Project Name
PROJECT_NAME = 'Art Bootstrap'
HOSTNAME = config('HOSTNAME', default='127.0.0.1:8000')


# Social Media Links
FACEBOOK_URL = 'https://www.facebook.com/artbootstrap'
TWITTER_URL = 'https://twitter.com/ArtBootstrap'
INSTAGRAM_URL = 'https://instagram.com/artbootstrap'
PINTEREST_URL = 'https://pinterest.com/artbootstrap'


# Start-up fixtures
FIXTURES = ['categories', 'technology']


# Paypal
PAYPAL_CURRENCY_CODE = 'USD'


# Sendgrid
SENDGRID_API_KEY = config('SENDGRID_API_KEY')


# Robots
ROBOTS_CACHE_TIMEOUT = 60 * 60 * 24  # 24 hours


# Django AutoField
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

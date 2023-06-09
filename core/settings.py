import os

from pathlib import Path
from decouple import config, Csv
from django.core.management.utils import get_random_secret_key
from celery.schedules import crontab


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = config('DEBUG', default=True, cast=bool)
SECRET_KEY = config('SECRET_KEY', default=get_random_secret_key())
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())
INTERNAL_IPS = config('INTERNAL_IPS', default='127.0.0.1', cast=Csv())
CSRF_TRUSTED_ORIGINS = ['http://ecom.com']

CELERY_BROKER_URL = config('CELERY_BROKER_URL', default='redis://localhost:6379/0')
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BEAT_SCHEDULE = {
    'Get currencies privat': {
        'task': 'currencies.tasks.get_currencies_privat',
        'schedule': crontab(hour='13', minute='40'),
    },
    'Get currencies mono': {
        'task': 'currencies.tasks.get_currencies_mono',
        'schedule': crontab(hour='13', minute='41'),
    },
}

LOGIN_URL = 'profiles:login'
LOGIN_REDIRECT_URL = 'catalog:home'
LOGOUT_REDIRECT_URL = 'profiles:login'

AUTH_USER_MODEL = 'profiles.User'
AUTHENTICATION_BACKENDS = [
    'profiles.backends.EmailBackend',
    'profiles.backends.PhoneBackend'
]

CART_SESSION_ID = 'cart'

DEFAULT_CURRENCY = 'UAH'

PHONENUMBER_DB_FORMAT = 'INTERNATIONAL'
PHONENUMBER_DEFAULT_REGION = 'UA'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'daphne',
    'django.contrib.staticfiles',
    'rest_framework',
    'silk',
    'debug_toolbar',
    'redisboard',
    'django_celery_results',
    'django_celery_beat',
    'django_filters',
    'drf_yasg',
    'phonenumber_field',
    'widget_tweaks',
    'catalog',
    'cart',
    'contacts',
    'core',
    'currencies',
    'favorites',
    'orders',
    'profiles',
    'profiles.signup',
    'profiles.password',
    'profiles.password.change',
    'profiles.password.reset',
    'reviews',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'silk.middleware.SilkyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',

            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'
ASGI_APPLICATION = 'core.asgi.application'

DATABASES = {
    "default": {
        "ENGINE": 'django.db.backends.postgresql',
        "NAME": config("SQL_DATABASE", default="SQL_DATABASE"),
        "USER": config("SQL_USER", default="SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD", default="SQL_PASSWORD"),
        "HOST": config("SQL_HOST", default="SQL_HOST"),
        "PORT": config("SQL_PORT", default="5432"),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', }, # noqa
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', }, # noqa
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', }, # noqa
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },# noqa
]

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": "redis://redis:6379",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config('EMAIL_HOST', default='EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default='EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='EMAIL_HOST_PASSWORD') # noqa
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
# EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=True, cast=bool)
EMAIL_SIGNUP_TEMPLATE = 'profiles/signup/email.html'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Kiev'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = 'static_files'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = 'media/'
MEDIA_ROOT = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

try:
    from core.settings_local import *  # noqa
except ImportError:
    ...

# if DEBUG:
#     MIDDLEWARE += [
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     ]
#     INSTALLED_APPS += [
#         'debug_toolbar',
#     ]
#     INTERNAL_IPS = config('INTERNAL_IPS', default='127.0.0.1', cast=Csv())
#
#     import mimetypes
#     mimetypes.add_type("application/javascript", ".js", True)
#
#     DEBUG_TOOLBAR_CONFIG = {
#         'INTERCEPT_REDIRECTS': False,
#     }

# LOGGING = {
#     'version': 1,
#     'formatters': {
#         'verbose': {
#             'format': '%(levelname)s %(asctime)s '
#                       '%(module)s %(process)d %(thread)d %(message)s'
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',
#             'formatter': 'simple'
#         },
#         # 'file': {
#         #     'level': 'DEBUG',
#         #     'class': 'logging.FileHandler',
#         #     'filename': '/path/to/your/file.log',
#         #     'formatter': 'simple'
#         # },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     }
# }

# if DEBUG:
#     for logger in LOGGING['loggers']:
#         LOGGING['loggers'][logger]['handlers'] = ['console']

"""
Django settings for Artskill project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import oscar

from django.core.exceptions import ImproperlyConfigured


def root(*dirs):
    base_dir = os.path.join(os.path.dirname(__file__), '..', '..')
    return os.path.abspath(os.path.join(base_dir, *dirs))

def app_root(*dirs):
    return root('app', *dirs)


def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x2cgsvsif8#fzsuv()(w)kt%6p^9+)#wjlwbwdyiyji@df!3=*'
# DEBUG = True

ALLOWED_HOSTS = []

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'


BASE_DIR = root()


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = app_root('public/static/')
STATICFILES_DIRS = [
    app_root('static'),
]


MEDIA_URL = '/media/'
MEDIA_ROOT = app_root('public/media/')


LOGIN_REDIRECT_URL = '/'
APPEND_SLASH = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.flatpages',

    'widget_tweaks',
] + oscar.get_core_apps()

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            app_root('templates'),
            app_root('templates/oscar'),
            oscar.OSCAR_MAIN_TEMPLATE_DIR
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                # 'django.template.context_processors.i18n',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTHENTICATION_BACKENDS = [
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
]

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Haystack settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 'PATH': location('whoosh_index'),
    },
}

# Here's a sample Haystack config if using Solr (which is recommended)
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://127.0.0.1:8983/solr/',
#        'INCLUDE_SPELLING': True
#    },
#}


# ==============
# Oscar settings
# ==============

from oscar.defaults import *

# Meta
# ====

OSCAR_SHOP_NAME = 'Artskill'
# OSCAR_SHOP_TAGLINE = 'Tagline'

OSCAR_DEFAULT_CURRENCY = 'RUB'
# OSCAR_CURRENCY_FORMAT = {
#     'USD': {
#         'currency_digits': False,
#         'format_type': "accounting",
#     },
#     'EUR': {
#         'format': u'#,##0\xa0¤',
#     }
# }

# Order processing
# ================

# Sample order/line status settings. This is quite simplistic. It's like you'll
# want to override the set_status method on the order object to do more
# sophisticated things.
OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'

# This dict defines the new order statuses than an order can move to
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Complete', 'Cancelled',),
    'Cancelled': (),
    'Complete': (),
}
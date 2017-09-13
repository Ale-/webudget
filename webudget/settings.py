"""
Django settings for WeBudget project
"""

import os
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.abspath( os.path.dirname(__file__) )
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(ENV_PATH, '..', 'static')
PROJECT_STATIC_FOLDER = 'webudget'
STATICFILES_DIRS = [
    ( PROJECT_STATIC_FOLDER, STATIC_ROOT + '/' + PROJECT_STATIC_FOLDER + '/' ),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(ENV_PATH, '..', 'media')
MAINTENANCE_IGNORE_URLS = (
    r'^/admin/.*',
    r'^/login$',
)
LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_URL = '/logout'
LOGOUT_REDIRECT_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_OPEN = True

# Name of site in the document title
DOCUMENT_TITLE = 'WeBudget'
DOCUMENT_DESCRIPTION = _('WeBudget is a platform for participatory and transparent budgeting.')

# Sites conf
SITE_ID = 1

#
# Application definition
#

CONTRIB_APPS = [
    'django.contrib.sites',
    'django.contrib.admin',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'maintenancemode',
    'leaflet',
    'djgeojson',
    'django_countries',
]

PROJECT_APPS = [
    'apps.models',
    'apps.utils',
]

INSTALLED_APPS = CONTRIB_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webudget.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ 'templates' ],
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

WSGI_APPLICATION = 'webudget.wsgi.application'

#
# Password validation
#
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

#
# Internationalization
#
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('en', _('English')),
)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)
DECIMAL_SEPARATOR = '.'

#
# Restrict django-countries querysets to European countries
# from http://www.countrycallingcodes.com/iso-country-codes/europe-codes.php
#
COUNTRIES_ONLY = [ 'AL','AD','AT','BY','BE','BA','BG','HR','CY','CZ','DK','EE',
'FO','FI','FR','DE','GI','GR','HU','IS','IE','IM','IT','RS',
'LV','LI','LT','LU','MK','MT','MD','MC','ME','NL','NO','PL','PT','RO','RU',
'SM','RS','SK','SI','ES','SE','CH','UA','GB','VA','RS' ]

#
# Import private settings
#
from .private_settings import *

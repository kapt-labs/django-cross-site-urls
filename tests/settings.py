# -*- coding: utf-8 -*-

# Standard library imports
import os

TEST_ROOT = os.path.abspath(os.path.dirname(__file__))


class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return 'notmigrations'


DEBUG = False
TEMPLATE_DEBUG = False

SECRET_KEY = 'key'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:'
    },
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.sites',

    'rest_framework',
    'cross_site_urls',
    'tests',
]

MIGRATION_MODULES = DisableMigrations()
TEST_RUNNER = 'django.test.runner.DiscoverRunner'  # Hide checks

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
)

MEDIA_ROOT = '/media/'
STATIC_URL = '/static/'

USE_TZ = True
LANGUAGE_CODE = 'en'
LANGUAGES = (
    ('fr', 'Français'),
    ('en', 'English'),
)

SITE_ID = 1

ROOT_URLCONF = 'tests._testsite.urls'

# Setting this explicitly prevents Django 1.7+ from showing a
# warning regarding a changed default test runner. The test
# suite is run with py.test, so it does not matter.
SILENCED_SYSTEM_CHECKS = ['1_6.W001']

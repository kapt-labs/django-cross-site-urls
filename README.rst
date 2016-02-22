=======================
django-cross-site-urls
=======================

.. image:: http://img.shields.io/pypi/v/django-cross-site-urls.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-cross-site-urls/
    :alt: Latest Version

.. image:: http://img.shields.io/pypi/l/django-cross-site-urls.svg?style=flat-square
    :target: https://pypi.python.org/pypi/django-cross-site-urls/
    :alt: License

.. image:: http://img.shields.io/travis/kapt-labs/django-cross-site-urls.svg?style=flat-square
    :target: http://travis-ci.org/kapt-labs/django-cross-site-urls
    :alt: Build status

.. image:: http://img.shields.io/coveralls/kapt-labs/django-cross-site-urls.svg?style=flat-square
    :target: https://coveralls.io/r/kapt-labs/django-cross-site-urls
    :alt: Coveralls status

*A Django module allowing to resolve urls across two django sites.*

.. contents:: :local:

Requirements
------------

Python 2.7+ or 3.3+, Django 1.7+, Django REST framework >= 3.2.4.

Installation
-------------

Just run:

::

  pip install django-cross-site-urls

Once installed you just need to add ``cross_site_urls`` to ``INSTALLED_APPS`` in your project's settings module:

::

  INSTALLED_APPS = (
      # other apps
      'cross_site_urls',
  )

Add module configuration to urls of the two django sites:

::
  from cross_site_urls.conf import settings as cross_site_settings

::
  urlpatterns = i18n_patterns(
    # other urls patterns
    url((r'^{}').format(cross_site_settings.DEFAULT_API_URL), include('cross_site_urls.urls')),
  )

Configure required 'CROSS_SITE_URLS_SITES' settings

::
.. CROSS_SITE_URLS_SITES = {
..     'site_a': {
..         'domain': 'a.example.com',
..         'scheme': 'https',
..      },
..     'site_b': {
..         'domain': 'b.example.com',
..         'scheme': 'http',
..      },
.. }

*Congrats! You’re in.*

Authors
-------

Kapt <dev@kapt.mobi> and contributors_

.. _contributors: https://github.com/kapt-labs/django-cross-site-urls/contributors

License
-------

BSD. See ``LICENSE`` for more details.

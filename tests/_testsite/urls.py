# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Local application / specific library imports
from cross_site_urls.conf import settings as cross_site_settings

admin.autodiscover()

urlpatterns = i18n_patterns(
    '',
    url((r'^{}').format(cross_site_settings.DEFAULT_API_URL), include('cross_site_urls.urls')),
)

urlpatterns += staticfiles_urlpatterns()

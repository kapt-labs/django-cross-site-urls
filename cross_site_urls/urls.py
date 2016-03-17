# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import url

from .views import URLResolveAPIView
from .constants import RESOLVE_API_VIEW_URL


urlpatterns = patterns('',
                       url(r'^{}$'.format(RESOLVE_API_VIEW_URL), URLResolveAPIView.as_view(), name='resolve-url'))

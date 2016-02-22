# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from django.core.urlresolvers import reverse

from .constants import RESOLVE_API_VIEW_URL


def get_api_url(scheme, domain):
    resolve_view_url = reverse('resolve-url').replace(RESOLVE_API_VIEW_URL, '')
    return '{}://{}{}'.format(scheme, domain, resolve_view_url)

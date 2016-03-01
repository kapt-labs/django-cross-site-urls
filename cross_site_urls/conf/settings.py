# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

# Third party imports
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

# Local application / specific library imports

DEFAULT_SCHEME = getattr(settings, 'CROSS_SITE_URLS_DEFAULT_SCHEME', 'http')

DEFAULT_API_URL = getattr(settings, 'CROSS_SITE_URLS_DEFAULT_API_URL', 'urls/')

VERIFY_SSL_CERT = getattr(settings, 'CROSS_SITE_URLS_VERIFY_SSL_CERT', True)

# The following setting should define the related sites configuration
# It should contains a dictionary defining each related site:
#
# CROSS_SITE_URLS_SITES = {
#     'site_a': {
#         'domain': 'a.example.com',
#         'scheme': 'https',
#      },
#     'site_b': {
#         'domain': 'b.example.com',
#         'scheme': 'http',
#      },
# }
#
# Please note that scheme is optional.
# Defaults values are: CROSS_SITE_URLS_DEFAULT_SCHEME setting
SITES = getattr(settings, 'CROSS_SITE_URLS_SITES', {})

for k in SITES.keys():
    site = SITES[k]

    if 'domain' not in site:
        raise ImproperlyConfigured("[Cross site] Configuration error: No domain configured for site {}".format(k))

    if 'scheme' not in site:
        SITES[k]['scheme'] = DEFAULT_SCHEME

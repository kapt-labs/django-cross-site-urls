# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals
import uuid
import requests

from django.core.exceptions import ImproperlyConfigured
from django.utils import translation

import slumber

from .conf import settings as local_settings
from .encoding import prefix_kwargs
from .utils import get_api_url
from .constants import RESOLVE_API_VIEW_URL


def resolve_url(site_id, view_name, args=None, kwargs=None):

    if site_id not in local_settings.SITES:
        raise ImproperlyConfigured("[Cross site] Configuration error: The given site identifier is not configured in the settings")

    site_conf = local_settings.SITES[site_id]
    language = translation.get_language()

    resolve_args = {'view_name': view_name,
                    'args': args,
                    'language': language}

    if kwargs:
        kwargs_prefix = uuid.uuid4()
        resolve_args["kwargs_prefix"] = kwargs_prefix
        prefixed_kwargs = prefix_kwargs(kwargs_prefix, kwargs)
        resolve_args.update(prefixed_kwargs)

    api_url = get_api_url(site_conf["scheme"],
                          site_conf["domain"])

    session = requests.Session()
    session.verify = local_settings.VERIFY_SSL_CERT
    api = slumber.API(api_url, session=session, auth=local_settings.API_AUTH_CREDENTIALS)

    resolver = RESOLVE_API_VIEW_URL.replace('/', '')
    url = getattr(api, resolver).get(**resolve_args)['url']
    return url

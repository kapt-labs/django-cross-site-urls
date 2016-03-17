# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import uuid

from cross_site_urls.encoding import prefix_kwargs
from cross_site_urls.encoding import unprefix_kwargs


class TestPrefixUnPrefixKwargs(object):
    def test_prefix_kwargs_can_be_unprefixed(self):
        kwargs = {'key1': 'value1',
                  'key2': 'value2'}
        prefix = str(uuid.uuid4())
        prefixed_kwargs = prefix_kwargs(prefix, kwargs)

        unprefixed_kwargs = unprefix_kwargs(prefix, prefixed_kwargs)
        assert kwargs == unprefixed_kwargs

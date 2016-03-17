# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from cross_site_urls.encoding import prefix_kwargs
from cross_site_urls.encoding import unprefix_kwargs


class TestPrefixKwargs(object):
    def test_can_prefix_kwargs(self):
        kwargs = {'key1': 'value1',
                  'key2': 'value2'}
        prefix = 'prefix'
        prefixed_kwargs = prefix_kwargs(prefix, kwargs)

        assert prefixed_kwargs == {'prefix_key1': 'value1',
                                   'prefix_key2': 'value2'}


class TestUnPrefixKwargs(object):
    def test_can_unprefix_kwargs(self):
        prefixed_kwargs = {'prefix_key1': 'value1',
                           'prefix_key2': 'value2'}
        prefix = 'prefix'
        kwargs = unprefix_kwargs(prefix, prefixed_kwargs)

        assert kwargs == {'key1': 'value1',
                          'key2': 'value2'}

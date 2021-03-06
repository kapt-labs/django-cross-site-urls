# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from cross_site_urls.utils import get_api_url


class TestGetAPIUrlUtils(object):
    def test_can_retrieve_api_url(self):
        url = get_api_url('http', 'example.com')
        assert url == 'http://example.com/en/urls/'

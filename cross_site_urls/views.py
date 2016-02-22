# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

from django.utils import translation
from django.conf import settings

from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from cross_site_urls.encoding import unprefix_kwargs


class URLResolveAPIView(APIView):
    """
    Returns the resolved url that match the given url kwargs.
    """

    def get(self, request):
        view_name = request.GET.get("view_name", None)
        language = request.GET.get("language", None)

        if view_name is None or language is None:
            raise ParseError("[Cross site] Invalid call")
        args = request.GET.getlist('args')
        kwargs_prefix = request.GET.get("kwargs_prefix", None)

        kwargs = unprefix_kwargs(kwargs_prefix, request.GET) if kwargs_prefix is not None else {}

        current_language_code = translation.get_language()

        if language in dict(settings.LANGUAGES):
            translation.activate(language)
        data = {'url': reverse(view_name, args=args, kwargs=kwargs, request=request)}
        translation.activate(current_language_code)

        return Response(data)

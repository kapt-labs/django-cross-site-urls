# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals

import sys

# Third party imports
from django import template
from django.template.base import Node
from django.template.base import TemplateSyntaxError
from django.template.base import kwarg_re
from django.utils.encoding import smart_text
from django.conf import settings
from django.utils import six

# Local application / specific library imports
from cross_site_urls.urlresolvers import resolve_url

register = template.Library()


class URLNode(Node):
    def __init__(self, site_id, view_name, args, kwargs, asvar):
        self.site_id = site_id
        self.view_name = view_name
        self.args = args
        self.kwargs = kwargs
        self.asvar = asvar

    def render(self, context):
        from django.core.urlresolvers import reverse, NoReverseMatch
        args = [arg.resolve(context) for arg in self.args]
        kwargs = dict((smart_text(k, 'ascii'), v.resolve(context))
                      for k, v in self.kwargs.items())

        site_id = self.site_id.resolve(context)
        view_name = self.view_name.resolve(context)

        # Try to look up the URL twice: once given the view name, and again
        # relative to what we guess is the "main" app. If they both fail,
        # re-raise the NoReverseMatch unless we're using the
        # {% url ... as var %} construct in which case return nothing.
        url = ''
        try:

            url = resolve_url(site_id, view_name, args=args, kwargs=kwargs)
        except NoReverseMatch:
            exc_info = sys.exc_info()
            if settings.SETTINGS_MODULE:
                project_name = settings.SETTINGS_MODULE.split('.')[0]
                try:
                    url = reverse(project_name + '.' + view_name,
                                  args=args, kwargs=kwargs)
                except NoReverseMatch:
                    if self.asvar is None:
                        # Re-raise the original exception, not the one with
                        # the path relative to the project. This makes a
                        # better error message.
                        six.reraise(*exc_info)
            else:
                if self.asvar is None:
                    raise

        if self.asvar:
            context[self.asvar] = url
            return ''
        else:
            return url


@register.tag
def cross_url(parser, token):
    """
    Resolves an URL of a remote site in a template.
    Usage::
        {% load cross_site_urls %}
        {% cross_url 'site-identifier' "url_name" arg1 arg2' %}
        or
        {% cross_url "url_name" name1=value1 name2=value2 %}
    """
    bits = token.split_contents()
    if len(bits) < 3:
        raise TemplateSyntaxError("'%s' takes at least two argument, a site name and the name of a url()." % bits[0])
    site_identifier = parser.compile_filter(bits[1])
    viewname = parser.compile_filter(bits[2])
    args = []
    kwargs = {}
    asvar = None
    bits = bits[3:]
    if len(bits) >= 2 and bits[-2] == 'as':
        asvar = bits[-1]
        bits = bits[:-2]

    if len(bits):
        for bit in bits:
            match = kwarg_re.match(bit)
            if not match:
                raise TemplateSyntaxError("Malformed arguments to url tag")
            name, value = match.groups()
            if name:
                kwargs[name] = parser.compile_filter(value)
            else:
                args.append(parser.compile_filter(value))
    return URLNode(site_identifier, viewname, args, kwargs, asvar)

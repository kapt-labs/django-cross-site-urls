# -*- coding:utf-8 -*-

# Standard library imports
from __future__ import unicode_literals


def prefix_kwargs(prefix, kwargs):
    prefixed_kwargs = {}
    for k, v in kwargs.items():
        prefixed_key = '{}_{}'.format(prefix, k)
        prefixed_kwargs[prefixed_key] = v
    return prefixed_kwargs


def unprefix_kwargs(prefix, kwargs):
    unprefixed_kwargs = {}
    for k, v in kwargs.items():
        if k.startswith(prefix):
            unprefixed_key = k[len(prefix) + 1:]
            unprefixed_kwargs[unprefixed_key] = v
    return unprefixed_kwargs

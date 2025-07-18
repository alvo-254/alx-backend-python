#!/usr/bin/env python3
"""Utils module"""

import requests


def get_json(url):
    """Fetch JSON data from a URL"""
    response = requests.get(url)
    return response.json()


def memoize(method):
    """Simple memoization decorator"""
    attr_name = "_{}".format(method.__name__)

    @property
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, method(self))
        return getattr(self, attr_name)
    return wrapper

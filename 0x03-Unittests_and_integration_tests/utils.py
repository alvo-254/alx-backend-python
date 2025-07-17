#!/usr/bin/env python3
"""utils module"""

import requests


def get_json(url):
    """Fetch JSON data from a URL"""
    response = requests.get(url)
    return response.json()

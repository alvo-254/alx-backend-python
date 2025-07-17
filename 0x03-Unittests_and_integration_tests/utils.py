#!/usr/bin/env python3
"""Utils module"""

import requests


def access_nested_map(nested_map, path):
    """Access nested map using a tuple path"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map


def get_json(url):
    """Get JSON from a REST API"""
    response = requests.get(url)
    return response.json()

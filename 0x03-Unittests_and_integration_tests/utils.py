#!/usr/bin/env python3
"""Utils module"""


def access_nested_map(nested_map, path):
    """Access nested map using a sequence of keys."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map

#!/usr/bin/env python3
"""utils module"""

def access_nested_map(nested_map, path):
    """Access nested map with path"""
    for key in path:
        nested_map = nested_map[key]
    return nested_map

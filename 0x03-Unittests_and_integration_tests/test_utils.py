#!/usr/bin/env python3
"""Unittest module for utils"""

import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns correct values"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), TypeError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Test access_nested_map raises correct exceptions"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)

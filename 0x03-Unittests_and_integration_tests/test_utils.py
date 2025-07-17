#!/usr/bin/env python3
"""Unittests for access_nested_map in utils.py"""

import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function"""

    def test_access_nested_map(self):
        """Test valid map paths"""
        self.assertEqual(access_nested_map({"a": 1}, ("a",)), 1)
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ("a",)), {"b": 2})
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ("a", "b")), 2)

    def test_access_nested_map_exception(self):
        """Test that KeyError or TypeError are raised for invalid paths"""
        with self.assertRaises(KeyError):
            access_nested_map({}, ("a",))

        with self.assertRaises(TypeError):
            access_nested_map({"a": 1}, ("a", "b"))

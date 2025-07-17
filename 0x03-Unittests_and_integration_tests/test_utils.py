#!/usr/bin/env python3
"""Unittest module for utils"""

import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Unit tests for access_nested_map"""

    def test_access_nested_map(self):
        """Test valid inputs to access_nested_map"""
        self.assertEqual(access_nested_map({"a": 1}, ("a",)), 1)
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ("a",)), {"b": 2})
        self.assertEqual(access_nested_map({"a": {"b": 2}}, ("a", "b")), 2)

    def test_access_nested_map_exception(self):
        """Test exceptions for invalid keys"""
        with self.assertRaises(KeyError):
            access_nested_map({}, ("a",))
        with self.assertRaises(TypeError):
            access_nested_map({"a": 1}, ("a", "b"))

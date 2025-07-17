#!/usr/bin/env python3
"""Unittests for utils.py"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test the get_json function"""

    @parameterized.expand([
        ("test1", "http://example.com", {"payload": True}),
        ("test2", "http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, name, url, expected, mock_get):
        """Test that get_json returns the expected result"""
        mock_get.return_value.json.return_value = expected
        self.assertEqual(get_json(url), expected)

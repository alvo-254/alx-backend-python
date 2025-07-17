#!/usr/bin/env python3
"""Test utils module"""
import unittest
from unittest.mock import patch
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Test class for memoize decorator"""

    def test_memoize(self):
        """Test that memoize decorator caches results properly"""
        class TestClass:
            """Test class with memoized property"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                         return_value=42) as mock_method:
            test_instance = TestClass()
            
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            
            mock_method.assert_called_once()

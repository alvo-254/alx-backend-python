#!/usr/bin/env python3
"""Test utils module"""
import unittest
from unittest.mock import patch, Mock
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

        # Create instance of test class
        test_instance = TestClass()

        # Patch the a_method to track calls and return fixed value
        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            # First call - should call a_method
            self.assertEqual(test_instance.a_property, 42)
            
            # Second call - should return cached result
            self.assertEqual(test_instance.a_property, 42)
            
            # Verify a_method was called only once
            mock_method.assert_called_once()

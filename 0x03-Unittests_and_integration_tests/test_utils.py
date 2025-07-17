#!/usr/bin/env python3
"""Unit tests for utils.memoize"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from utils import memoize


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches the result of a method"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_method:
            mock_method.return_value = 42
            test = TestClass()

            # Call memoized method twice
            result_1 = test.a_property
            result_2 = test.a_property

            mock_method.assert_called_once()
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

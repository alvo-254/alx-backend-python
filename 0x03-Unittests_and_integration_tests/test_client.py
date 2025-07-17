#!/usr/bin/env python3
"""Unit tests for client module"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch("client.get_json")
    def test_org(self, org_name, expected, mock_get_json):
        """Test GithubOrgClient.org with mock"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(org_name)
        result = client.org()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()

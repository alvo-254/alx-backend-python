#!/usr/bin/env python3
"""Unittest for GithubOrgClient.org"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """Test the org method with mocked get_json"""
        mock_get_json.return_value = expected

        client = GithubOrgClient(org_name)
        result = client.org()

        self.assertEqual(result, expected)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


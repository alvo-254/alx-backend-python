#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class."""

import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.GithubOrgClient.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_payload = {"org_name": org_name}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    def test_public_repos_url(self):
        """Test that GithubOrgClient._public_repos_url returns the expected URL."""
        test_payload = {"repos_url": "https://api.github.com/orgs/test_org/repos"}
        with patch('client.GithubOrgClient.org', return_value=test_payload):
            client = GithubOrgClient("test_org")
            self.assertEqual(client._public_repos_url,
                            test_payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
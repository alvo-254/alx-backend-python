#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized

from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
        ("alx-africa",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct data."""
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test public_repos method returns list of repo names."""
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient, "org", new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {"repos_url": "http://fake.url/repos"}

            client = GithubOrgClient("test_org")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_get_json.assert_called_once_with("http://fake.url/repos")


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Unit tests for client.py"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct payload"""
        expected_payload = {"login": org_name}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_payload)
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """Test that _public_repos_url returns correct value"""
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

        client = GithubOrgClient("google")
        result = client._public_repos_url
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test that public_repos returns the correct list of repos"""
        mock_repos_url.return_value = "https://api.github.com/orgs/google/repos"
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        client = GithubOrgClient("google")
        result = client.public_repos()
        expected = ["repo1", "repo2", "repo3"]

        self.assertEqual(result, expected)
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")
        mock_repos_url.assert_called_once()


if __name__ == "__main__":
    unittest.main()

    @patch("client.get_json")
    @patch("client.GithubOrgClient._public_repos_url", new_callable=PropertyMock)
    def test_public_repos_with_license(self, mock_repos_url, mock_get_json):
        """Test public_repos filters by license"""
        mock_repos_url.return_value = "https://api.github.com/orgs/google/repos"
        mock_get_json.return_value = [
            {
                "name": "repo1",
                "license": {"key": "apache-2.0"}
            },
            {
                "name": "repo2",
                "license": {"key": "mit"}
            },
            {
                "name": "repo3",
                "license": {"key": "apache-2.0"}
            },
        ]

        client = GithubOrgClient("google")
        result = client.public_repos(license="apache-2.0")
        expected = ["repo1", "repo3"]

        self.assertEqual(result, expected)
        mock_get_json.assert_called_once()
        mock_repos_url.assert_called_once()

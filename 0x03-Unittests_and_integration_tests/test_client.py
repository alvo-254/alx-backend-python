#!/usr/bin/env python3
"""Unit tests for GithubOrgClient class."""

import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value."""
        test_payload = {"org_name": org_name}
        mock_get_json.return_value = test_payload
        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test _public_repos_url returns the expected URL."""
        test_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = test_payload
            client = GithubOrgClient("test_org")
            self.assertEqual(
                client._public_repos_url,
                test_payload["repos_url"]
            )
            mock_org.assert_called_once()

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos returns the expected list of repo names."""
        test_repos_url = "https://api.github.com/orgs/test_org/repos"
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_get_json.return_value = test_payload
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos_url:
            mock_public_repos_url.return_value = test_repos_url
            client = GithubOrgClient("test_org")
            self.assertEqual(client.public_repos, ["repo1", "repo2"])
            mock_get_json.assert_called_once_with(test_repos_url)
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other"}}, "my_license", False),
        ({}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license returns the correct boolean."""
        client = GithubOrgClient("test_org")
        self.assertEqual(
            client.has_license(repo, license_key),
            expected
        )


if __name__ == "__main__":
    unittest.main()

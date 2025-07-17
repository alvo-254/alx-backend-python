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
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct payload"""
        test_payload = {"login": org_name, "repos_url": f"https://api.github.com/orgs/{org_name}/repos"}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org(), test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test that _public_repos_url returns correct value"""
        with patch('client.GithubOrgClient.org', new_callable=PropertyMock) as mock_org:
            test_payload = {"repos_url": "https://api.github.com/orgs/google/repos"}
            mock_org.return_value = test_payload

            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result, test_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method"""
        test_payload = [{"name": "repo1", "license": {"key": "mit"}}, 
                       {"name": "repo2", "license": {"key": "apache-2.0"}}]
        mock_get_json.return_value = test_payload

        with patch('client.GithubOrgClient._public_repos_url',
                 new_callable=PropertyMock) as mock_public_repos_url:
            test_url = "https://api.github.com/orgs/google/repos"
            mock_public_repos_url.return_value = test_url

            client = GithubOrgClient("google")
            # Test without license filter
            self.assertEqual(client.public_repos(), ["repo1", "repo2"])
            # Test with license filter
            self.assertEqual(client.public_repos(license_key="mit"), ["repo1"])
            mock_get_json.assert_called_once_with(test_url)
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
        ({"license": {}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()

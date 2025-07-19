#!/usr/bin/env python3
"""Integration tests for GithubOrgClient class."""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
import requests
import json
import os

@parameterized_class([
    {
        "org_payload": {"login": "google", "id": 1},
        "repos_payload": [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
            {"name": "repo3"}
        ],
        "expected_repos": ["repo1", "repo2", "repo3"],
        "expected_has_license": [True, True, False]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient using fixtures."""

    @classmethod
    def setUpClass(cls):
        """Set up class by patching requests.get."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        # Setup the side effects for requests.get to return the fixture payloads
        def side_effect(url, *args, **kwargs):
            if url == "https://api.github.com/orgs/google":
                response = unittest.mock.Mock()
                response.json.return_value = cls.org_payload
                return response
            elif url == "https://api.github.com/orgs/google/repos":
                response = unittest.mock.Mock()
                response.json.return_value = cls.repos_payload
                return response
            return unittest.mock.Mock()

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Stop patcher after all tests."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns expected repo names."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos, self.expected_repos)

    def test_has_license(self):
        """Test has_license returns expected results per repo."""
        client = GithubOrgClient("google")
        for repo, expected in zip(self.repos_payload, self.expected_has_license):
            self.assertEqual(client.has_license(repo, "apache-2.0") or client.has_license(repo, "mit"), expected)

if __name__ == "__main__":
    unittest.main()
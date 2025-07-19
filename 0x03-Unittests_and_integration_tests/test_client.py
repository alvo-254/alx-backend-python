#!/usr/bin/env python3
"""Integration tests for GithubOrgClient."""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient

@parameterized_class([
    {
        "org_payload": {"login": "google", "id": 1},
        "repos_payload": [
            {"name": "repo1", "license": {"key": "apache-2.0"}},
            {"name": "repo2", "license": {"key": "mit"}},
            {"name": "repo3"}
        ],
        "expected_repos": ["repo1", "repo2", "repo3"]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient with fixtures."""

    @classmethod
    def setUpClass(cls):
        """Set up patcher for requests.get."""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url, *args, **kwargs):
            if url == "https://api.github.com/orgs/google":
                mock_resp = unittest.mock.Mock()
                mock_resp.json.return_value = cls.org_payload
                return mock_resp
            elif url == "https://api.github.com/orgs/google/repos":
                mock_resp = unittest.mock.Mock()
                mock_resp.json.return_value = cls.repos_payload
                return mock_resp
            return unittest.mock.Mock()

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_public_repos(self):
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos, self.expected_repos)

if __name__ == "__main__":
    unittest.main()
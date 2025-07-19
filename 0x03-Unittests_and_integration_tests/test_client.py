#!/usr/bin/env python3
"""Integration test for GithubOrgClient.public_repos"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient
import json

# Load payloads from the fixtures
with open("fixtures/org_payload.json", "r") as f:
    org_payload = json.load(f)

with open("fixtures/repos_payload.json", "r") as f:
    repos_payload = json.load(f)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": [repo["name"] for repo in repos_payload],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos with fixtures"""

    @classmethod
    def setUpClass(cls):
        """Start patching get_json"""
        cls.get_patcher = patch("client.get_json", side_effect=[
            cls.org_payload,
            cls.repos_payload
        ])
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Stop patching"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos returns correct repo names"""
        client = GithubOrgClient("test-org")
        self.assertEqual(client.public_repos(), self.expected_repos)

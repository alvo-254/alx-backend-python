#!/usr/bin/env python3
"""Unit tests for client module"""
import unittest
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that public_repos returns the correct list"""
        # Payload to be returned by mocked get_json
        mock_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = mock_payload

        # Patch the _public_repos_url property
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_url:
            mock_url.return_value = "https://api.github.com/orgs/test_org/repos"

            # Instantiate the client
            client = GithubOrgClient("test_org")
            result = client.public_repos()

            # Assert the result matches names in payload
            expected = ["repo1", "repo2", "repo3"]
            self.assertEqual(result, expected)

            # Assert calls
            mock_get_json.assert_called_once()
            mock_url.assert_called_once()

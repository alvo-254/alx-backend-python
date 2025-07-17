class TestGithubOrgClient(unittest.TestCase):
    """Test case for GithubOrgClient class."""

    @patch('client.get_json')
    def test_org(self, mock_get_json):
        """Test GithubOrgClient.org returns the correct data."""
        test_payload = {"login": "alx"}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient("alx")
        result = client.org

        self.assertEqual(result, test_payload)
        mock_get_json.assert_called_once_with("https://api.github.com/orgs/alx")

    def test_public_repos_url(self):
        """Test that _public_repos_url returns the correct value from org."""
        with patch.object(GithubOrgClient, 'org', new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": "https://api.github.com/orgs/alx/repos"}
            client = GithubOrgClient("alx")
            result = client._public_repos_url
            self.assertEqual(result, "https://api.github.com/orgs/alx/repos")

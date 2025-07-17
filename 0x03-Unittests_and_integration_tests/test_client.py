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

from utils import get_json

class GithubOrgClient:
    """GithubOrgClient class to interact with GitHub API"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        """Fetch organization data from GitHub"""
        return get_json(self.ORG_URL.format(self.org_name))

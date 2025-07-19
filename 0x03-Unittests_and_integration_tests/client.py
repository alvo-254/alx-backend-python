from utils import get_json
from utils import memoize


class GithubOrgClient:
    """GitHub Org client"""

    def __init__(self, org_name):
        self.org_name = org_name

    @memoize
    def org(self):
        """Get org details from GitHub API"""
        return get_json(f"https://api.github.com/orgs/{self.org_name}")

    @property
    def _public_repos_url(self):
        """Get repos_url from org payload"""
        return self.org["repos_url"]

    def public_repos(self):
        """Return list of public repo names"""
        repos = get_json(self._public_repos_url)
        return [repo["name"] for repo in repos]

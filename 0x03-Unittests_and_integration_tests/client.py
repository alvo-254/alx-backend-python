from utils import get_json
from utils import memoize

class GithubOrgClient:
    """GitHub Org client"""

    def __init__(self, org_name):
        self.org_name = org_name

    @memoize
    def org(self):
        return get_json(f"https://api.github.com/orgs/{self.org_name}")

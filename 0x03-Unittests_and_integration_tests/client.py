#!/usr/bin/env python3
"""GithubOrgClient module"""

from utils import get_json


class GithubOrgClient:
    """GithubOrgClient class"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        """Fetch org data"""
        return get_json(self.ORG_URL.format(self.org_name))

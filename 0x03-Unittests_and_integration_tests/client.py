#!/usr/bin/env python3
"""Client module"""

from utils import get_json


class GithubOrgClient:
    """Client for GitHub organization"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name):
        self.org_name = org_name

    def org(self):
        """Get the organization info"""
        return get_json(self.ORG_URL.format(org=self.org_name))

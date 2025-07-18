#!/usr/bin/env python3
"""Client module"""

from utils import get_json, memoize


class GithubOrgClient:
    """GitHub Organization Client"""
    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org_name):
        self.org_name = org_name

    @memoize
    def org(self):
        """Return organization data"""
        return get_json(self.ORG_URL.format(self.org_name))

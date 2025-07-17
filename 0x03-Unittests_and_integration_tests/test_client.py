#!/usr/bin/env python3
"""GithubOrgClient module"""

import requests
from typing import List, Dict


class GithubOrgClient:
    """GitHub organization client"""
    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org_name: str) -> None:
        self.org_name = org_name

    @property
    def _public_repos_url(self) -> str:
        org_data = self.org()
        return org_data["repos_url"]

    def org(self) -> Dict:
        return get_json(self.ORG_URL.format(org=self.org_name))

    def public_repos(self, license: str = None) -> List[str]:
        repos = get_json(self._public_repos_url)
        repo_names = [
            repo["name"] for repo in repos
            if not license or self.has_license(repo, license)
        ]
        return repo_names

    @staticmethod
    def has_license(repo: Dict, license_key: str) -> bool:
        """Checks if a repo has the specified license"""
        return repo.get("license", {}).get("key") == license_key

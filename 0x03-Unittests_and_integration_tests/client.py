#!/usr/bin/env python3
"""GithubOrgClient module"""
from typing import Dict, List
import requests
from utils import get_json, memoize


class GithubOrgClient:
    """GithubOrgClient class"""

    ORG_URL = "https://api.github.com/orgs/{}"

    def __init__(self, org: str) -> None:
        """Initialize with org name"""
        self.org_name = org

    @memoize
    def org(self) -> Dict:
        """Get organization details"""
        return get_json(self.ORG_URL.format(self.org_name))

    @property
    def _public_repos_url(self) -> str:
        """Get public repos url from org data"""
        return self.org.get("repos_url")

    def public_repos(self, license: str = None) -> List[str]:
        """List public repos for the org"""
        repos_data = get_json(self._public_repos_url)
        repo_names = [repo["name"] for repo in repos_data]

        if license:
            return [
                repo["name"]
                for repo in repos_data
                if repo.get("license", {}).get("key") == license
            ]
        return repo_names

    @staticmethod
    def has_license(repo: Dict, license_key: str) -> bool:
        """Check if repo has specified license"""
        return repo.get("license", {}).get("key") == license_key

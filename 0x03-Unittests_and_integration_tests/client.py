#!/usr/bin/env python3
"""Github Org Client"""

from urllib.request import urlopen
import json
from typing import Dict, List, Union


def get_json(url: str) -> Dict:
    """Get JSON from remote URL"""
    with urlopen(url) as response:
        return json.loads(response.read())


class GithubOrgClient:
    """Github org client"""

    def __init__(self, org_name: str):
        """Initialize client"""
        self._org_name = org_name

    @property
    def org(self) -> Dict:
        """Get organization info"""
        return get_json(f"https://api.github.com/orgs/{self._org_name}")

    @property
    def _public_repos_url(self) -> str:
        """Get public repos URL"""
        return self.org["repos_url"]

    def public_repos(self, license_key: str = None) -> List[str]:
        """Get public repositories"""
        repos = get_json(self._public_repos_url)
        if license_key:
            return [
                repo["name"] for repo in repos
                if self.has_license(repo, license_key)
            ]
        return [repo["name"] for repo in repos]

    @staticmethod
    def has_license(repo: Dict[str, Dict], license_key: str) -> bool:
        """Check if repo has license"""
        return repo.get("license", {}).get("key") == license_key

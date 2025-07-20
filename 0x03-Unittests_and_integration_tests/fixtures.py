org_payload = {
    "login": "google",
    "id": 1342004,
    "repos_url": "https://api.github.com/orgs/google/repos"
}

repos_payload = [
    {"id": 1, "name": "repo1", "license": {"key": "apache-2.0"}},
    {"id": 2, "name": "repo2", "license": {"key": "other"}},
    {"id": 3, "name": "repo3", "license": {"key": "apache-2.0"}},
    {"id": 4, "name": "repo4", "license": None}
]

expected_repos = ["repo1", "repo2", "repo3", "repo4"]

apache2_repos = ["repo1", "repo3"]
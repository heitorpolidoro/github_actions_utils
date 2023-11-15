import os
from typing import Tuple

from git import Repo
from github import Github
from github.Auth import Token
from github.Repository import Repository


def get_gh_repo(token=None) -> Repository:
    token = token or os.getenv("GITHUB_TOKEN")
    gh = Github(auth=Token(token))
    repo = Repo(os.getcwd())
    # Get the URL of the 'origin' remote
    remote_url = repo.remotes.origin.url

    owner, repo_name = extract_owner_and_repo_name(remote_url)

    return gh.get_repo(f"{owner}/{repo_name}")


def extract_owner_and_repo_name(remote_url) -> Tuple[str, str]:
    # Extract the owner and repository name from the URL
    owner, repo_name = remote_url.split("/")[-2:]
    # Remove '.git' from the repo_name if it's there
    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]
    return owner, repo_name

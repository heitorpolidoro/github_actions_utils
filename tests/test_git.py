import pytest

from github_actions_utils.git import get_gh_repo, extract_owner_and_repo_name


@pytest.fixture(scope="module")
def vcr_cassette_name(request):
    return "get_repo.yaml"


@pytest.mark.vcr
def test_get_gh_repo(monkeypatch):
    monkeypatch.setenv("GITHUB_TOKEN", "github_token")
    repo = get_gh_repo()
    assert repo.name == "github_actions_utils"
    assert repo.owner.login == "heitorpolidoro"


def test_extract_owner_and_repo_name_with_dot_git():
    owner, repo_name = extract_owner_and_repo_name(
        "https://github.com/heitorpolidoro/github_actions_utils.git"
    )
    assert repo_name == "github_actions_utils"
    assert owner == "heitorpolidoro"


def test_extract_owner_and_repo_name_without_dot_git():
    owner, repo_name = extract_owner_and_repo_name(
        "https://github.com/heitorpolidoro/github_actions_utils"
    )
    assert repo_name == "github_actions_utils"
    assert owner == "heitorpolidoro"

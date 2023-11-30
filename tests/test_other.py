import tempfile

import pytest

from github_actions_utils import set_output


@pytest.fixture(autouse=True)
def github_env(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        monkeypatch.setenv("GITHUB_OUTPUT", temp.name)
        yield temp.name


def test_set_output(github_env):
    set_output("TEST", "test")
    with open(github_env, "r") as f:
        assert f.read() == "TEST=test"

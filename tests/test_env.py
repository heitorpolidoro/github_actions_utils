import os
import tempfile

import pytest

from github_actions_utils import set_env, get_env, inputs, github_envs
from github_actions_utils.env import PrefixEnv


@pytest.fixture(autouse=True)
def github_env(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        monkeypatch.setenv("GITHUB_ENV", temp.name)
        yield temp.name


@pytest.fixture(autouse=True)
def clean_environ():
    yield
    if "TEST_ENV" in os.environ:
        del os.environ["TEST_ENV"]


def test_set_env(github_env):
    assert os.getenv("TEST_ENV") is None
    set_env("TEST_ENV", "test")
    with open(github_env, "r") as f:
        assert f.read() == "TEST_ENV=test"


def test_set_env_in_environ():
    assert os.getenv("TEST_ENV") is None
    set_env("TEST_ENV", "test")
    assert os.getenv("TEST_ENV") == "test"


def test_get_env_not_existing():
    set_env("TEST_ENV", "test")
    assert get_env("TEST_NO_ENV") is None


def test_get_env(monkeypatch):
    monkeypatch.setenv("TEST_ENV", "test")
    assert get_env("TEST_ENV") == "test"


def test_get_env_bool(monkeypatch):
    monkeypatch.setenv("TEST_ENV", "true")
    assert get_env("TEST_ENV", type=bool) is True


def test_get_env_int(monkeypatch):
    monkeypatch.setenv("TEST_ENV", "42")
    assert get_env("TEST_ENV", type=int) == 42


def test_get_env_default(monkeypatch):
    assert get_env("TEST_ENV", default=42) == 42


def test_get_env_casting_default(monkeypatch):
    assert get_env("TEST_ENV", default=True, type=bool) is True


def test_get_env_casting_without_default(monkeypatch):
    assert get_env("TEST_ENV", type=int) is None


def test_get_env_from_github_env():
    assert get_env("TEST_ENV") is None
    set_env("TEST_ENV", "test")
    del os.environ["TEST_ENV"]
    assert get_env("TEST_ENV") == "test"


def test_inputs(monkeypatch):
    monkeypatch.setenv("INPUT_PARAM", "value")
    assert inputs.param == "value"


def test_github_envs(monkeypatch):
    monkeypatch.setenv("GITHUB_ENV", "value")
    assert github_envs.env == "value"


def test_prefix_env_to_upper_false(monkeypatch):
    monkeypatch.setenv("prefixed_env", "value")
    prefixed = PrefixEnv("prefixed", to_upper=False)
    assert prefixed.env == "value"

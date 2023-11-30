import tempfile
from unittest.mock import patch

import pytest

from github_actions_utils import (
    set_output,
    append_summary,
    overwrite_summary,
    erase_summary,
)
from github_actions_utils.other import add_system_path


@pytest.fixture(autouse=True)
def github_output(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        monkeypatch.setenv("GITHUB_OUTPUT", temp.name)
        yield temp.name


@pytest.fixture(autouse=True)
def summary(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        monkeypatch.setenv("GITHUB_STEP_SUMMARY", temp.name)
        yield temp.name


def test_set_output(github_output):
    set_output("TEST", "test")
    with open(github_output, "r") as f:
        assert f.read() == "TEST=test"


def test_append_summary(summary):
    append_summary("test append 1")
    append_summary("test append 2")
    with open(summary, "r") as f:
        assert f.read() == "test append 1\ntest append 2\n"


def test_overwrite_summary(summary):
    append_summary("test overwrite.png 1")
    overwrite_summary("test overwrite.png 2")
    with open(summary, "r") as f:
        assert f.read() == "test overwrite.png 2\n"


def test_erase_summary(summary):
    append_summary("test erase 1")
    erase_summary()
    append_summary("test erase 2")
    with open(summary, "r") as f:
        assert f.read() == "test erase 2\n"


def test_double_erase_summary():
    erase_summary()
    erase_summary()


def test_erase_summary_without_env(monkeypatch):
    with patch("github_actions_utils.env.get_env", return_value=None):
        erase_summary()


def test_add_system_path(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        monkeypatch.setenv("GITHUB_PATH", temp.name)
        add_system_path("test")
        with open(temp.name, "r") as f:
            assert f.read() == "test\n"

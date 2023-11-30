from unittest.mock import patch, call

import pytest

from github_actions_utils import (
    debug,
    notice,
    warning,
    error,
    start_group,
    end_group,
    group,
    mask,
)


@pytest.fixture(autouse=True)
def mock_print():
    with patch("builtins.print") as mock_print:
        yield mock_print


def test_debug(mock_print):
    debug("test")
    mock_print.assert_called_with("::debug ::test")


def test_notice(mock_print):
    notice("test", file="file", line=1, end_line=2)
    mock_print.assert_called_with("::notice file=file,line=1,endLine=2::test")


def test_warning(mock_print):
    warning("test", file="file", line=1, end_line=2)
    mock_print.assert_called_with("::warning file=file,line=1,endLine=2::test")


def test_error(mock_print):
    error("test", file="file", line=1, end_line=2)
    mock_print.assert_called_with("::error file=file,line=1,endLine=2::test")


def test_start_group(mock_print):
    start_group("test")
    mock_print.assert_called_with("::group ::test")


def test_end_group(mock_print):
    end_group()
    mock_print.assert_called_with("::endgroup ::")


def test_group_context(mock_print):
    with group("test"):
        print("Inside the group")
    mock_print.assert_has_calls(
        [call("::group ::test"), call("Inside the group"), call("::endgroup ::")]
    )


def test_group_context_exception(mock_print):
    with pytest.raises(Exception):
        with group("test"):
            raise Exception("test")
    mock_print.assert_has_calls([call("::group ::test"), call("::endgroup ::")])


def test_mask(mock_print):
    mask("test")
    mock_print.assert_called_with("::add-mask ::test")

import tempfile

import pytest

from github_actions_utils.log_utils import github_group, summary


@pytest.fixture
def github_step_summary(monkeypatch):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        monkeypatch.setenv("GITHUB_STEP_SUMMARY", temp.name)
        yield temp.name


def test_github_group_simple(capsys):
    @github_group("simple")
    def simple():
        print("Hello, world!")

    simple()
    out, err = capsys.readouterr()
    assert out == "::group::simple\nHello, world!\n::endgroup::\n"
    assert err == ""


def test_github_group_using_parameter_value(capsys):
    @github_group("$parameter_value")
    def using_parameter_value(parameter_value):
        print(parameter_value)

    using_parameter_value("Hello, world!")
    out, err = capsys.readouterr()
    assert out == "::group::Hello, world!\nHello, world!\n::endgroup::\n"
    assert err == ""


def test_github_group_using_parameter_value_with_multiple_parameters(capsys):
    @github_group("$parameter_value1 $parameter_value2")
    def using_parameter_value_with_multiple_parameters(
            parameter_value1, parameter_value2
    ):
        print(parameter_value1, parameter_value2)

    using_parameter_value_with_multiple_parameters("Hello,", "world!")
    out, err = capsys.readouterr()
    assert out == "::group::Hello, world!\nHello, world!\n::endgroup::\n"
    assert err == ""


def test_github_group_using_object_attributes(capsys):
    class TestObject:
        def __init__(self):
            self.attribute = "Hello, world!"

    @github_group("$(obj.attribute)")
    def using_object_attributes(obj):
        print(obj.attribute)

    test_object = TestObject()
    using_object_attributes(test_object)
    out, err = capsys.readouterr()
    assert out == "::group::Hello, world!\nHello, world!\n::endgroup::\n"
    assert err == ""


def test_summary_write(github_step_summary):
    summary("Test text", overwrite=False)
    with open(github_step_summary, "r") as f:
        assert f.read() == "Test text\n"


def test_summary_append(github_step_summary):
    summary("Test text", overwrite=False)
    with open(github_step_summary, "r") as f:
        assert f.read() == "Test text\n"

    summary("Test text 2", overwrite=False)
    with open(github_step_summary, "r") as f:
        assert f.read() == "Test text\nTest text 2\n"


def test_summary_overwrite(github_step_summary):
    summary("Test text", overwrite=False)
    with open(github_step_summary, "r") as f:
        assert f.read() == "Test text\n"

    summary("Test text 3", overwrite=True)
    with open(github_step_summary, "r") as f:
        assert f.read() == "Test text 3\n"

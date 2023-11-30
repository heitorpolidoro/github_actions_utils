import os
from typing import Any

from github_actions_utils import github


def set_output(name: str, value: Any):
    """
    Sets an output variable

    :param name: Name of the output variable.
    :param value: Value of the output variable.
    """
    with open(github.output, "w") as f:
        f.write(f"{name}={value}")


def append_summary(message: str):
    """
    Appends a message to the summary

    :param message: Message to append.
    """
    with open(github.step_summary, "a") as f:
        f.write(f"{message}\n")


def overwrite_summary(message: str):
    """
    Overwrites the summary

    :param message: Message to overwrite.png.
    """
    with open(github.step_summary, "w") as f:
        f.write(f"{message}\n")


def erase_summary():
    """
    Erases the summary
    """
    summary = github.step_summary
    if summary and os.path.exists(summary):
        os.remove(summary)


def add_system_path(path: str):
    """
    Adds a path to the system path

    :param path: Path to add.
    """
    with open(github.path, "a") as f:
        f.write(f"{path}\n")

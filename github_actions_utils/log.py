import re
from contextlib import contextmanager
from typing import Any


def _to_first_lower_pascal_case(snake_str: str) -> str:
    """
    Convert a snake_case string to PascalCase.
    :param snake_str: Snake case string
    :return: PascalCase string with the first letter lower cased.
    :rtype: str
    """
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), snake_str)


def print_command(
    command: str, message: str = "", **command_params: dict[str, Any]
) -> None:
    """
     Prints a command to the log in the format "::COMMAND [COMMAND_PARAM=COMMAND_PARAM_VALUE,...]::MESSAGE

    :param command: Command to print
    :param message: Message to print using the command
    :param command_params: The commands parameters
    """
    command_params_str = ",".join(
        f"{_to_first_lower_pascal_case(key)}={value}"
        for key, value in command_params.items()
        if value is not None
    )
    print(f"::{command} {command_params_str}::{message}")


def debug(message: str) -> None:
    """
    Prints a debug message
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-a-debug-message

    :param message: Message to print as debug
    """
    print_command("debug", message)


def notice(
    message: str,
    title: str = None,
    file: str = None,
    line: int = None,
    end_line: int = None,
    col: int = None,
    end_column: int = None,
) -> None:
    """
    Prints a notice message
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-a-notice-message

    :param message: Message to print as notice
    :param title: Custom title
    :param file: Filename
    :param line: Line number, starting at 1
    :param end_line: End line number
    :param col: Column number, starting at 1
    :param end_column: End column number
    """
    print_command("notice", **locals())


def warning(
    message: str,
    title: str = None,
    file: str = None,
    line: int = None,
    end_line: int = None,
    col: int = None,
    end_column: int = None,
) -> None:
    """
    Prints a warning message
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-a-warning-message

    :param message: Message to print as warning
    :param title: Custom title
    :param file: Filename
    :param line: Line number, starting at 1
    :param end_line: End line number
    :param col: Column number, starting at 1
    :param end_column: End column number
    """
    print_command("warning", **locals())


def error(
    message: str,
    title: str = None,
    file: str = None,
    line: int = None,
    end_line: int = None,
    col: int = None,
    end_column: int = None,
) -> None:
    """
    Prints an error message
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-error-message

    :param message: Message to print as error
    :param title: Custom title
    :param file: Filename
    :param line: Line number, starting at 1
    :param end_line: End line number
    :param col: Column number, starting at 1
    :param end_column: End column number
    """
    print_command("error", **locals())


def start_group(name: str) -> None:
    """
    Start a group log
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#grouping-log-lines

    :param name: Name of the group to start.
    """
    print_command("group", name)


def end_group() -> None:
    """
    End the current group log
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#grouping-log-lines
    """
    print_command("endgroup")


@contextmanager
def group(name: str):
    """
    Start and end a group log in a context manager
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#grouping-log-lines

    :param name: Name of the group.
    """
    start_group(name)
    try:
        yield
    finally:
        end_group()


def mask(value: str) -> None:
    """
    Mask a value it a log
    https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#masking-a-value-in-a-log

    :param value: Value to be masked
    """
    print_command("add-mask", value)

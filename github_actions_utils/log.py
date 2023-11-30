import re
from contextlib import contextmanager


def to_pascal_case(snake_str):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), snake_str)


def print_command(command: str, message: str = "", **command_params):
    command_params_str = ",".join(
        f"{to_pascal_case(key)}={value}" for key, value in command_params.items() if value is not None)
    print(f"::{command} {command_params_str}::{message}")


def debug(message: str) -> None:
    print_command("debug", message)


def notice(
        message: str,
        title: str = None,
        file: str = None,
        col: int = None,
        end_column: int = None,
        line: int = None,
        end_line: int = None,
) -> None:
    print_command("notice", **locals())


def warning(
        message: str,
        title: str = None,
        file: str = None,
        col: int = None,
        end_column: int = None,
        line: int = None,
        end_line: int = None,
) -> None:
    print_command("warning", **locals())


def error(
        message: str,
        title: str = None,
        file: str = None,
        col: int = None,
        end_column: int = None,
        line: int = None,
        end_line: int = None,
) -> None:
    print_command("error", **locals())


def start_group(name: str) -> None:
    print_command("group", name)


def end_group() -> None:
    print_command("endgroup")


@contextmanager
def group(name: str):
    start_group(name)
    try:
        yield
    finally:
        end_group()


def mask(value: str) -> None:
    print_command("add-mask", value)

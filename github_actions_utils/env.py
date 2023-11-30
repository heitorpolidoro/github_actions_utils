import os
from typing import Any, Callable


def _str_to_bool(s: str) -> bool:
    """Converts string to boolean"""
    return s.lower() in ["true", "1", "t", "y", "yes"]


def set_env(env_name: str, value: Any):
    """
    Sets an environment variable and writes it to the GitHub environment.

    :param env_name: The ENV name
    :param value: The ENV value
    """
    os.environ[env_name] = value
    with open(github.env, "w") as f:
        f.write(f"{env_name}={value}")


def _get_env_from_github_env(env_name: str) -> str | None:
    """
    Returns an environment variable from the GitHub environment

    :param env_name: The ENV name
    :return: The ENV value
    """
    value = None
    with open(os.getenv("GITHUB_ENV"), "r") as f:
        for line in f:
            if line.startswith(env_name):
                name, value = line.split("=")
                os.environ[name] = value

    return value


# noinspection PyShadowingBuiltins
def get_env(env: str, default: Any = None, type: Callable = None) -> Any:
    """
    Gets an environment variable, including from the GitHub environment
    Return the default value, if any
    Cato to the type, if any

    :param env: The Env name
    :param default: The default value
    :param type: The type to be casted to
    :return: The value of the ENV or the default value, if any, casted to the type, if any.
    None if the ENV is not set and no default value is provided.
    """
    value = os.getenv(env, default) or _get_env_from_github_env(env)
    if value is not None and type is not None:
        if type == bool and not isinstance(value, bool):
            value = _str_to_bool(value)
        else:
            value = type(value)
    return value


class PrefixEnv:
    """
    A class to get environment variables with a prefix
    """

    def __init__(self, prefix: str, to_upper: bool = True):
        """
        :param prefix: The prefix of the ENV
        :param to_upper: Whether to convert the ENV name to uppercase
        """
        self.prefix = prefix
        self.to_upper = to_upper

    def __getattr__(self, item):
        env_name = f"{self.prefix}_{item}"
        if self.to_upper:
            env_name = env_name.upper()
        return get_env(env_name)


github = PrefixEnv("GITHUB")  # TODO move to GithunPlus?
inputs = PrefixEnv("INPUT")

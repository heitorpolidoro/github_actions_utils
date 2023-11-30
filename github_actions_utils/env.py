import os
from typing import Any, Callable


def _str_to_bool(s: str) -> bool:
    """ Converts string to boolean """
    return s.lower() in ["true", "1", "t", "y", "yes"]


def set_env(env_name: str, value: Any):
    """
    Sets an environment variable and writes it to the GitHub environment.

    :param env_name:
    :param value:
    :return:
    """
    os.environ[env_name] = value
    with open(os.getenv("GITHUB_ENV"), "w") as f:
        f.write(f"{env_name}={value}")


def _get_env_from_github_env(env_name: str) -> str:
    """Returns an environment variable from the GitHub environment"""
    with open(os.getenv("GITHUB_ENV"), "r") as f:
        for line in f:
            if line.startswith(env_name):
                name, value = line.split("=")
                os.environ[name] = value

    return os.getenv(env_name)


# noinspection PyShadowingBuiltins
def get_env(env: str, default: Any = None, type: Callable = None) -> Any:
    """Gets an environment variable, including from the GitHub environment"""
    value = os.getenv(env, default) or _get_env_from_github_env(env)
    if type is not None:
        if type == bool:
            value = _str_to_bool(value)
        else:
            value = type(value)
    return value


class PrefixEnv:
    def __init__(self, prefix: str, to_upper: bool = True):
        self.prefix = prefix
        self.to_upper = to_upper

    def __getattr__(self, item):
        env_name = f"{self.prefix}_{item}"
        if self.to_upper:
            env_name = env_name.upper()
        return get_env(env_name)


github_envs = PrefixEnv("GITHUB")
inputs = PrefixEnv("INPUT")

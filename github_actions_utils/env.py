import os
from typing import Any

type_ = type


def _str_to_bool(s):
    return s.lower() in ["true", "1", "t", "y", "yes"]


def set_env(env_name: str, value: Any):
    os.environ[env_name] = value
    with open(os.getenv("GITHUB_ENV"), "w") as f:
        f.write(f"{env_name}={value}")


def _get_env_from_github_env(env_name: str):
    with open(os.getenv("GITHUB_ENV"), "r") as f:
        for line in f:
            if line.startswith(env_name):
                name, value = line.split("=")
                os.environ[name] = value

    return os.getenv(env_name)


# noinspection PyShadowingBuiltins
def get_env(env: str, default: Any = None, type: type_ = None) -> Any:
    value = os.getenv(env, default) or _get_env_from_github_env(env)
    if type is not None:
        if type == bool:
            value = _str_to_bool(value)
        else:
            value = type(value)
    return value
# TODO get all envs?
# class GithubEnvs:
#     def __getattr__(self, item):
#         return get_github_env(item.upper())
#
#
# class Inputs:
#     def __getattr__(self, item):
#         return get_input(item.upper())
#
# github_envs = GithubEnvs()
# inputs = Inputs()

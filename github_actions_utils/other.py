import os
from typing import Any


def set_output(name: str, value: Any):
    """Sets an output variable"""
    with open(os.getenv("GITHUB_OUTPUT"), "w") as f:
        f.write(f"{name}={value}")

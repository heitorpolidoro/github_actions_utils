import inspect
import os
import re
from string import Template
from typing import Callable, Any


def log_group(group_name: str) -> Callable:
    def wrapper(f: Callable) -> Callable:
        objects_attributes = []
        for var in re.findall(r"\$\([\w.]+\)", group_name):
            attribute = re.sub(r"\$\(([\w.]+)\)", "\\1", var)
            # attribute_template = attribute.replace(".", "_")
            objects_attributes.append(attribute)

        def inner_wrapper(*args, **kwargs):
            inner_group_name = group_name
            template_dict = kwargs.copy()
            for index, name in enumerate(inspect.signature(f).parameters):
                if index < len(args):
                    template_dict[name] = args[index]

            for object_attribute in objects_attributes:
                value = template_dict
                for attr in object_attribute.split("."):
                    if isinstance(value, dict):
                        value = value.get(attr, None)
                    else:
                        value = getattr(value, attr, None)
                attribute_template = object_attribute.replace(".", "_")
                template_dict[attribute_template] = value
                inner_group_name = re.sub(
                    rf"\$\({attribute}\)", f"${attribute_template}", inner_group_name
                )

            print(
                f"::group::{Template(inner_group_name).safe_substitute(**template_dict)}"
            )
            resp = f(*args, **kwargs)
            print("::endgroup::")
            return resp

        return inner_wrapper

    return wrapper


def summary(text: str, overwrite: bool = False, end: str = "\n"):
    summary_file_path = os.getenv("GITHUB_STEP_SUMMARY")

    # Open the file in append mode
    mode = "w" if overwrite else "a"
    with open(summary_file_path, mode) as f:
        # Write to the file
        f.write(f"{text}{end}")


def summary_exec(action: str, check: Callable[[Any], bool]):
    def wrapper(f):
        def inner_wrapper(*args, **kwargs):
            summary(f"{action}...", end="")
            resp = f(*args, **kwargs)
            if check(resp):
                summary(":white_check_mark:")
            else:
                summary(":x:")
            return resp

        return inner_wrapper

    return wrapper

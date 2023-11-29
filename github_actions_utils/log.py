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
# from typing import Callable, Any, List
#
# from github_actions_utils.env import github_envs
#
#
# def extract_attributes(group_name: str) -> List[str]:
#     objects_attributes = []
#     for var in re.findall(r"\$\([\w.]+\)", group_name):
#         attribute = re.sub(r"\$\(([\w.]+)\)", "\\1", var)
#         objects_attributes.append(attribute)
#
#     return objects_attributes
#
#
# def generate_template_dict(objects_attributes, func, args, kwargs):
#     template_dict = {}
#     # Get the parameters names and values
#     for index, (name, param) in enumerate(inspect.signature(func).parameters.items()):
#         if index < len(args):
#             template_dict[name] = args[index]
#         else:
#             template_dict[name] = kwargs.get(name, param.default)
#
#     # Get the values from objects
#     for object_attribute in objects_attributes:
#         value = template_dict
#         for attr in object_attribute.split("."):
#             if isinstance(value, dict):
#                 value = value.get(attr, None)
#             else:
#                 value = getattr(value, attr, None)
#         template_dict[object_attribute.replace(".", "_")] = value
#     return template_dict
#
#
# def fix_objects_identifiers(group_name, objects_attributes):
#     inner_group_name = group_name
#     for object_attribute in objects_attributes:
#         attribute_template = object_attribute.replace(".", "_")
#         inner_group_name = re.sub(
#             rf"\$\({object_attribute}\)", f"${attribute_template}", inner_group_name
#         )
#     return inner_group_name
#
#
# def summary(text: str, overwrite: bool = False, end: str = "\n"):
#     summary_file_path = github_envs.step_summary
#
#     # Open the file in append mode
#     mode = "w" if overwrite else "a"
#     with open(summary_file_path, mode) as f:
#         # Write to the file
#         f.write(f"{text}{end}")
#
#
# def github_log_group(group_name: str) -> Callable:
#     # summary_check = summary_check or default_summary_check
#
#     objects_attributes = extract_attributes(group_name)
#
#     def wrapper(func: Callable) -> Callable:
#         def inner_wrapper(*args, **kwargs):
#             template_dict = generate_template_dict(
#                 objects_attributes, func, args, kwargs
#             )
#             inner_group_name = fix_objects_identifiers(group_name, objects_attributes)
#
#             text = Template(inner_group_name).safe_substitute(**template_dict)
#             print(f"::group::{text}")
#             resp = func(*args, **kwargs)
#             print("::endgroup::")
#             return resp
#
#         return inner_wrapper
#
#     return wrapper
#
#
# def summary_exec(action: str, check: Callable[[Any], bool] | bool = True):
#     def wrapper(f):
#         def inner_wrapper(*args, **kwargs):
#             summary(f"{action}...", end="")
#             try:
#                 resp = f(*args, **kwargs)
#                 if isinstance(check, bool) and check or callable(check) and check(resp):
#                     summary(":white_check_mark:")
#                 else:
#                     summary(":x:")
#                 return resp
#             except Exception as e:
#                 summary(":x:")
#                 summary(str(e))
#                 raise
#
#         return inner_wrapper
#
#     return wrapper

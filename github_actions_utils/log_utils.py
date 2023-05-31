import inspect
import re
from string import Template


def gitlab_group(group_name):
    def wrapper(f):
        params = []
        for var in re.findall(r'\$(\w+)', group_name):
            if var in inspect.signature(f).parameters:
                params.append(var)

        def inner_wrapper(*args, **kwargs):
            template_dict = {}
            args = list(args)
            for param in params:
                if param in kwargs:
                    template_dict[param] = kwargs[param]
                    continue
                for index, name in enumerate(inspect.signature(f).parameters):
                    if param == name:
                        template_dict[name] = args[index]
            print(f"::group::{Template(group_name).safe_substitute(**template_dict)}")
            resp = f(*args, **kwargs)
            print("::endgroup::")
            return resp

        return inner_wrapper

    return wrapper

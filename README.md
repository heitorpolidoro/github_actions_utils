# Github Actions Utils

![GitHub last commit](https://img.shields.io/github/last-commit/heitorpolidoro/github_actions_utils)
[![Latest](https://img.shields.io/github/release/heitorpolidoro/github_actions_utils.svg?label=latest)](https://github.com/heitorpolidoro/github_actions_utils/releases/latest)
![GitHub Release Date](https://img.shields.io/github/release-date/heitorpolidoro/github_actions_utils)
![GitHub commits since latest release (by SemVer including pre-releases)](https://img.shields.io/github/commits-since/heitorpolidoro/github_actions_utils/latest)<br>
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)<br>
![GitHub](https://img.shields.io/github/license/heitorpolidoro/github_actions_utils)

Github Actions Utils is a Python library to help creating actions

---

### Log utils

### `debug(message)`

### `notice(message, title=None, file=None, col=None, end_column=None, line=None, end_line=None)`

### `warning(message, title=None, file=None, col=None, end_column=None, line=None, end_line=None)`

### `error(message, title=None, file=None, col=None, end_column=None, line=None, end_line=None)`

```python
from github_actions_utils.log import debug, notice, warning, error

debug("This is a debug")

notice("This is a notice")
notice("This is a file notice with title", title="Nice Title", file=filename)

warning("This is a warning")
warning("This is a file warning with title", title="Nice Title", file=filename)

error("This is a error")
error("This is a file error with title", title="Nice Title", file=filename)
```

In the Action log:<br>
![Log](images/log.png)

In the Action summary:<br>
![Annotations](images/annotations.png)

In the Files changes when a file is passed as a parameter:<br>
![In file](images/in_file.png)

---

### `start_group(name)`

### `end_group()`

### `group(name)`

```python
from github_actions_utils.log import start_group, end_group

start_group("Group title")
print("logs inside group")
end_group()

# OR
from github_actions_utils.log import group

with group("Group title"):
    print("logs inside group")
```

![Group](images/group.png)

---

### `mask(value)`

Mask:

```python
from github_actions_utils.log import mask

mask("This is a mask")
print("Test This is a mask")
```

![Mask](images/mask.png)

---

### `set_env(env_name, value)`

### `get_env(env_name, default=None, type=None)`

```python
from github_actions_utils.log import set_env, get_env

set_env("ENV_NAME", "env_value")
get_env("ENV_NAME")  # == "env_value"

get_env("ENV_DEFAULT", default="default")  # == "default"

set_env("ENV_INT", "42")
get_env("ENV_INT, type=int")  # == 42

set_env("ENV_BOOL", "true")
get_env("ENV_BOOL, type=bool")  # == True

```

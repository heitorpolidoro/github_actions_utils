---
id: 4xx1ody5
title: README
file_version: 1.1.3
app_version: 1.18.41
---

# Github Actions Utils

<br/>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2Fdfafb002-e3e0-4e5d-ae39-275179c2fef6.png?alt=media&token=e4edecc1-57e3-438a-bb0e-8f32a668a07f" style="width:'50%'"/></div>

<br/>

[div align="center"](https://github.com/heitorpolidoro/github_actions_utils/releases/latest)

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2F9850ab75-4ca2-4a36-990d-874526251c44.png?alt=media&token=f91bba7c-6446-479e-a7e6-8b367a842547" style="width:'50%'"/></div>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2F912142eb-36ba-44db-937c-5c2165a230a9.png?alt=media&token=cbcb7722-a21a-44b4-8c6c-aa4727435003" style="width:'50%'"/></div>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2F5de2510c-0c49-40d7-87eb-6604ba91cf4c.png?alt=media&token=4be994c9-e156-4df5-8de8-809816f35672" style="width:'50%'"/></div>

<br/>

<br> [div align="center"](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2F1b206816-f9c5-4ab0-bf7c-35b1811de952.png?alt=media&token=02249d31-d900-4663-adaa-27833859e2f5" style="width:'50%'"/></div>

<br/>

<br>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2Fdd7fd52a-9ab3-4df7-bf9a-a4011e56b5b8.png?alt=media&token=94935db5-0fa0-49d1-a5cf-55886d710387" style="width:'50%'"/></div>

<br/>

<br/>

Github Actions Utils is a Python library to help creating actions

## Messages

### `debug(message)`

### `notice(message, title=None, file=None, line=None, end_line=None, col=None, end_column=None)`

### `warning(message, title=None, file=None, line=None, end_line=None, col=None, end_column=None)`

### `error(message, title=None, file=None, line=None, end_line=None, col=None, end_column=None)`

Write messages in the Action log, annotation or file \[[GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-a-debug-message)\]<br> In the Action log:<br>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2Fd533da27-476b-423c-9ec6-88b17e1ccca5.png?alt=media&token=45c4946b-2cfd-4024-966b-565170067d7a" style="width:'50%'"/></div>

<br/>

<br/>

In the Action summary:<br>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2Fb2ed41be-a6e1-42b3-9a3a-7e2edf9b80e3.png?alt=media&token=0fd4b450-60fe-40b5-912a-a9994e3b5a47" style="width:'50%'"/></div>

<br/>

<br/>

In the Files changes when a file is passed as a parameter:<br>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2Fa68f8399-6dbc-4744-ba06-2d36c9e8ee69.png?alt=media&token=7bb64635-07f0-45be-a9bb-e751c136b621" style="width:'50%'"/></div>

<br/>

<br/>

Usage:

```
from github_actions_utils import debug, notice, warning, error

debug("This is a debug")

notice("This is a notice")
notice("This is a file notice with title", title="Nice Title", file=filename)

warning("This is a warning")
warning("This is a file warning with title", title="Nice Title", file=filename)

error("This is a error")
error("This is a file error with title", title="Nice Title", file=filename)
```

## Group

### `start_group(name)`

### `end_group()`

### `group(name)`

Create a group log in Action log \[[GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#grouping-log-lines)\]<br>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2F289512b2-fa33-4917-ace9-12ba7ba2b27d.png?alt=media&token=908416e2-fd71-465d-8bad-57141fe31cb4" style="width:'50%'"/></div>

<br/>

<br/>

Usage:

```
from github_actions_utils import start_group, end_group

start_group("Group title")
print("logs inside group")
end_group()

# OR
from github_actions_utils import group

with group("Group title"):
    print("logs inside group")
```

## Mask

### `mask(value)`

Masks some secret value to avoid beem printed in the log \[[GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#masking-a-value-in-a-log)\]<br>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2Ffdb072dc-2583-40b5-951e-14d5edfc26b1.png?alt=media&token=3e086f7e-ebed-4654-993c-5b64683e74f6" style="width:'50%'"/></div>

<br/>

<br/>

Usage:

```
from github_actions_utils import mask

mask("This is a mask")
print("Test This is a mask")
```

## Environment Variables

### `set_env(env_name, value)`

### `get_env(env_name, default=None, type=None)`

Set and get environments variables, writing and reading in the default environment and from `GITHUB_ENV` file \[[GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#environment-files)\]<br> Usage:

```
from github_actions_utils import set_env, get_env

set_env("ENV_NAME", "env_value")
get_env("ENV_NAME")  # == "env_value"

get_env("ENV_DEFAULT", default="default")  # == "default"

set_env("ENV_INT", "42")
get_env("ENV_INT, type=int")  # == 42

set_env("ENV_BOOL", "true")
get_env("ENV_BOOL, type=bool")  # == True
```

## Output Parameter

### `set_output(name, value)`

Set an output value to be used in another steps \[[GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter)\]<br> Usage:

```
from github_actions_utils import set_output

set_output("NAME", "Heitor")
```

## Summary

### `append_summary(message)`

### `overwrite_summary(message)`

### `erase_summary()`

Write content in the job summary \[[GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#adding-a-job-summary)\]<br>

<br/>

<div align="center"><img src="https://firebasestorage.googleapis.com/v0/b/swimmio-content/o/repositories%2FZ2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw%3D%3D%2F8b84c8a5-dc47-4d0d-810a-b9afabfc03b9.png?alt=media&token=593290d3-7768-4c3d-8ef9-387920f5575a" style="width:'50%'"/></div>

<br/>

<br> Usage:

<br/>

```
from github_actions_utils import append_summary, overwrite_summary, erase_summary

append_summary("This is a list")
append_summary("- item 1")
append_summary("""- item 2
- item 3""")

overwrite_summary("No more list")

erase_summary()
```

## System Path

### `add_system_path(path)`

Prepends a directory to the system PATH \[[GitHub Docs](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#adding-a-system-path)\]<br>

<br/>

This file was generated by Swimm. [Click here to view it in the app](https://app.swimm.io/repos/Z2l0aHViJTNBJTNBZ2l0aHViX2FjdGlvbnNfdXRpbHMlM0ElM0FoZWl0b3Jwb2xpZG9ybw==/docs/4xx1ody5).

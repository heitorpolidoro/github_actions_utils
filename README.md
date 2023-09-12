# Github Actions Utils
![GitHub last commit](https://img.shields.io/github/last-commit/heitorpolidoro/github_actions_utils)
[![Latest](https://img.shields.io/github/release/heitorpolidoro/github_actions_utils.svg?label=latest)](https://github.com/heitorpolidoro/github_actions_utils/releases/latest)
![GitHub Release Date](https://img.shields.io/github/release-date/heitorpolidoro/github_actions_utils)

[![CI/CD](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/ci_cd.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)

![GitHub](https://img.shields.io/github/license/heitorpolidoro/github_actions_utils)

### Log Utils
#### github group decorator
```python
from github_actions_utils.log_utils import github_group

@github_group("foo")
def foo():
    code
```
Will produce in github action log
```log
▸ foo
```
You can use the function parameters as input like:
```python
@github_group("Running $cmd")
def run(cmd):
    code
```
When your code calls the `run` function will print user the value from `cmd` parameter:
```python
run("nice command")
```
```log
▸ Running nice command
```
Even if the value is an object and you want a value from the object attribute:
```python
@github_group("Hello $(person.name)")
def hello(person):
    code
```
```python
p = Person(name="Heitor")
hello(p)
```
```log
▸ Hello Heitor
```

# Github Actions Utils
![GitHub last commit](https://img.shields.io/github/last-commit/heitorpolidoro/github_actions_utils)
[![Latest](https://img.shields.io/github/release/heitorpolidoro/github_actions_utils.svg?label=latest)](https://github.com/heitorpolidoro/github_actions_utils/releases/latest)
![GitHub Release Date](https://img.shields.io/github/release-date/heitorpolidoro/github_actions_utils)

[![CI/CD](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/ci_cd.yml/badge.svg)](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/ci_cd.yml)
[![Code Quality](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/ci_cd.yml/badge.svg?event=issues)](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/ci_cd.yml)
[![Code Quality](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/ci_cd.yml/badge.svg?event=pull_request)](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/ci_cd.yml)

[![CI/CD](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/release.yml/badge.svg)](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/release.yml)
[![Code Quality](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/release.yml/badge.svg?event=issues)](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/release.yml)
[![Code Quality](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/release.yml/badge.svg?event=pull_request)](https://github.com/heitorpolidoro/github_actions_utils/actions/workflows/release.yml)

<a href="https://sonarcloud.io/project/overview?id=heitorpolidoro_github_actions_utils" >
  <img src="https://community.finos.org/img/vendors/sonarcloud-logo.png" alt="Sonarcloud" style="width:300px;">
</a>

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)

[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=coverage)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=heitorpolidoro_github_actions_utils&metric=bugs)](https://sonarcloud.io/summary/new_code?id=heitorpolidoro_github_actions_utils)


<a href="https://coveralls.io/github/heitorpolidoro/github_actions_utils">
  <img src="https://camo.githubusercontent.com/e66287f3f07172ea5536b34b3c4d02b03dee5901aecd641bb15b95549dfdd147/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f6173736574732e636f766572616c6c732e696f2f636f766572616c6c735f6c6f676f747970652d30312e706e67" alt="Sonarcloud" style="width:300px">
</a>

[![Coverage Status](https://coveralls.io/repos/github/heitorpolidoro/github_actions_utils/badge.svg?branch=master)](https://coveralls.io/github/heitorpolidoro/github_actions_utils?branch=master)

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

[![Build Status](https://travis-ci.org/{{cookiecutter.repo_name}}.svg?branch=master)](https://travis-ci.org/{{cookiecutter.repo_name}})
[![Coverage Status](https://coveralls.io/repos/github/{{cookiecutter.repo_name}}/badge.svg)](https://coveralls.io/github/{{cookiecutter.repo_name}})
[![codecov](https://codecov.io/gh/{{cookiecutter.repo_name}}/branch/master/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.repo_name}})
[![Requirements Status](https://requires.io/github/{{cookiecutter.repo_name}}/requirements.svg?branch=master)](https://requires.io/github/{{cookiecutter.repo_name}}/requirements/?branch=master)
[![PyUP](https://pyup.io/repos/github/{{cookiecutter.repo_name}}/shield.svg)](https://pyup.io/repos/github/{{cookiecutter.repo_name}})
[![PyPI](https://img.shields.io/pypi/pyversions/{{cookiecutter.project_name}}.svg)]()

Project for merging different file types, as example easy thumbnail image and unpacking archive in one field

# Installation

```bash
pip install {{cookiecutter.project_name}}

```

or from git

```bash
pip install -e git+{{cookiecutter.repo_url}}.git#egg={{cookiecutter.project_name}}
```

## Django and python version

* python-2.7 - django>=1.8,<=1.11
* python-3.4 - django>=1.8,<=1.11
* python-3.5 - django>=1.8,<=1.11
* python-3.6 - django>=1.11


# Usage



# Contributing

## run example app

```bash
pip install -r requirements.txt
./test/manage.py migrate
./test/manage.py runserver
```

## run tests

```bash
pip install -r requirements.txt
pytest
tox
```

## publish pypi

```bash
python setup.py sdist upload -r pypi
```







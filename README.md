# Cookiecutter Django App Starter

[![Build Status](https://travis-ci.org/Apkawa/cookiecutter-django-app-starter.svg?branch=master)](https://travis-ci.org/cookiecutter-django-app-starter)

A cookiecutter_ template for creating reusable Django packages (installable apps) quickly.

**Why?** Creating reusable Django packages has always been annoying. There are no defined/maintained
best practices (especially for ``setup.py``), so you end up cutting and pasting hacky, poorly understood,
often legacy code from one project to the other. This template, inspired by `cookiecutter-pypackage`_,
is designed to allow Django developers the ability to break free from cargo-cult configuration and follow
a common pattern dictated by the experts and maintained here.

* [Cookiecutter](https://github.com/audreyr/cookiecutter)
* [cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)

Features
--------

* Sane setup.py for easy PyPI registration/distribution
* Travis-CI configuration
* Codecov configuration
* Tox configuration
* Sphinx Documentation
* BSD licensed by default

Usage
-----

First, create your empty repo on Github (in our example below, we would call it ``blogging_for_humans``) and set up your virtual environment with your favorite method.

install Cookiecutter.

    $ pip install cookiecutter

Now run it against this repo

    $ cookiecutter https://github.com/apkawa/cookiecutter-django-app-starter.git

## Running Tests

Code has been written, but does it actually work? Let's find out!

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install -r requirements/tests.txt
    (myenv) $ py.test

## Setting up Travis

You will need to explicitly activate your repo in your `Travis CI profile`_.
If the repo isn't showing up, run a manual synchronisation.

[Travis CI profile](https://travis-ci.org/profile/)

## Integration with codecov.io

Code coverage is integrated with `Codecov`_. Make sure you have an account
and that you've granted access to your repo. In case of a private repo, you
will need to generate a token and pass it when submitting coverage.

[CodeCov](https://codecov.io/)

## Register on PyPI

Once you've got at least a prototype working and tests running, it's time to register the app on PyPI

    python setup.py register


## Releasing on PyPI

Time to release a new version? Easy!

First, use `bumpversion` to up the release number

    $ pip install bumpversion
    $ bumpversion --current-version VERSION_NUMBER minor --config-file setup.cfg

Where `VERSION_NUMBER` is the current version, e.g. `0.1.0`.

Then run

    $ python setup.py publish

It will answer with something like

You probably want to also tag the version now:

          git tag -a 0.1.0 -m 'version 0.1.0'
          git push --tags

Go ahead and follow those instructions.

## Add to Django Packages

Once you have a release, and assuming you have an account there,
just go to https://www.djangopackages.com/packages/add/ and add it there.


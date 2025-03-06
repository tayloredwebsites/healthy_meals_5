# healthy_meals: Meet your Dietary Goals with Healthier Meals

[![CircleCI](https://dl.circleci.com/status-badge/img/circleci/BZR3uzdbU6P9JdMbhCLMmZ/PhQcorR5decQrvhgn17chH/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/circleci/BZR3uzdbU6P9JdMbhCLMmZ/PhQcorR5decQrvhgn17chH/tree/main)
[![Coverage Status](https://tayloredwebsites.github.io/healthy_meals_5/qa/coverage/coverage_badge.svg)](https://tayloredwebsites.github.io/√/qa/coverage/html/index.html)
[![Test Status](https://tayloredwebsites.github.io/healthy_meals_5/qa/tests/tests_badge.svg)](https://tayloredwebsites.github.io/healthy_meals_5/qa/tests/index.html)
[![](https://tayloredwebsites.github.io/healthy_meals_5/qa/flake8/flake8_badge.svg)](https://tayloredwebsites.github.io/healthy_meals_5/qa/flake8/html/index.html)
[![](https://tayloredwebsites.github.io/healthy_meals_5/mypy_badge.svg)](https://tayloredwebsites.github.io/healthy_meals_5/qa/mypy/index.html)

[Documentation]("https://tayloredwebsites.github.io/healthy_meals_5/index.html")

## 🚀 Base Project Features
- Runs in Docker or locally
- Nox tool to run tests and test coverage
- Circle CI integration to ensure all tests pass for pull requests
- Django 5.1 & Python 3.12
- Sign in by email and password (see: [Lithium README](./LITHIUM_README.md))
- Github pages site for Documentation, Test Results, & Coverage
- Test and coverage badges in README.md
- Internationalization (i18n) of strings in code
- Soft Delete functionality of database records
- Base HTML Template
  - sub-template blocks for pages and partial pages
  - SCSS translation to CSS
  - site wide font sizing tool
  - login with email/password
  - signup

### Base Project Features coming soon:
- Internationalization (i18n) of strings in database
- Static typing checks with MyPy
- Sphinx documentation tool
- HTMX ?

### Application Features coming soon:


## Table of Contents
* [Installation](#installation)
* [Development Environment](#development-environment)
* [Next Steps](#next-steps)
* [Contributing](#contributing)
* [Support](#support)
* [License](#license)

## Installation

### 1) fork and clone repo(sitory) from github


    # cd <your_projects_parent_directory>

see: [Fork a Github Repo](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)

see: [Clone a Github Repo](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

    #confirm you are in your projects parent directory
    $ pwd #confirm you are in your projects parent directory
    $ git clone git@github.com:<yourGithubUsername>/healthy_meals.git
    $ cd healthy_meals
    $ git remote add upstream git@github.com:tayloredwebsites/healthy_meals.git

###  2) Installation of ASDF

    $ cat .tool-versions
      # you should see (with possible version differences):
      #    python 3.12.6
      #    direnv 2.34.0

### 3) installation of venv and direnv (working with asdf)

see: # [https://mdaverde.com/posts/python-venv-direnv-asdf/](https://mdaverde.com/posts/python-venv-direnv-asdf/)

    $ cd <code folder>
    $ cd healthy_meals  # see clone repo from github
    $ python -m venv .venv
    $ echo "export VIRTUAL_ENV=$PWD/.venv\nexport PATH=$PWD/.venv/bin:\$PATH" > .envrc
      # you should get: error ... .envrc is blocked. Run `direnv allow` to approve its content
    $ direnv allow
    $ which python3
      # you should see python3 3 running from the .venv directory
      #   .../healthy_meals/.venv/bin/python3
    $ cd ..
    $ cd healthy_meals
      # you will see the following messages entering your directory
      #   direnv: loading .../.envrc
      #   direnv: export +VIRTUAL_ENV ~PATH

### 4) install required software into .venv

    $ pip install -r requirements.txt

### 5) install postgres locally

Note: you may skip this step if you will be only using docker.

for brew install on mac: [https://daily-dev-tips.com/posts/installing-postgresql-on-a-mac-with-homebrew/](https://daily-dev-tips.com/posts/installing-postgresql-on-a-mac-with-homebrew/)

for other installs: [https://www.enterprisedb.com/docs/supported-open-source/postgresql/installing/](https://www.enterprisedb.com/docs/supported-open-source/postgresql/installing/)


Note: If you are having problems with installing postgres onto your computer, consider using docker desktop


### 6) install docker desktop

Note: You may skip this step if you are only developing locally.

## Development Environment Guide

### Docker Development

### Local Development

## Next Steps

### Base (Starter) Project Possible Enhancements
- Internationalization (i18n) of strings in database
- Static typing checks with MyPy
- Sphinx documentation tool
- HTMX ?
- Other enhancements ?

### Start Application Coding

#### 1) References Table

- This table will be designed to be able to have foreign key access to the references behind any particular piece of data or information on the site

#### 2) Consumables Table

- This table will be designed so that all variety of consumables such as food, supplements, herbs, medicines will be in this system.

#### 3) Consumable Aspects Table

- This table will be used to keep track of the important dietary aspects of consumables.  This will include:
  - Vitamins
  - Minerals
  - Nutrients
  - Anti-nutrients (such as oxalates).
  - Additives
  - Preservatives
- The amounts from the aspect's sample analysis will be stored such that an average value and variance of the aspect will be available for display

#### 4) and so on.

## Contributing

Please enter issues or pull requests (initially) for the following:
- Documentation issues, updates, or feature requests
- Base Starter branch issues, updates, or feature requests
- Application feature requests

If you are interested in contributing to the software development, please email [Dave Taylor of Taylored Web Sites](mailto:tayloredwebsites@me.com)
## License

Copyright (C) 2025 David A. Taylor of Taylored Web Sites (tayloredwebsites.com)
Licensed under [AGPL-3.0-only](https://opensource.org/license/agpl-v3/), and let me know how you wish to help.

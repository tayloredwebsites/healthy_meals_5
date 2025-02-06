# healthy_meals: A Django-Powered Diet Support Website to help make and eat healthier meals to meet your goals

[![Tests Status](./tests-badge.svg)](https://htmlpreview.github.io/?https://github.com/tayloredwebsites/healthy_meals/blob/main/reports/junit/index.html)
[![Coverage Status](./coverage-badge.svg)](https://htmlpreview.github.io/?https://github.com/tayloredwebsites/healthy_meals/blob/main/reports/coverage_html/index.html)

## 🚀 Features
- Built upon the Lithium Django Starter Project ([Lithium README](./LITHIUM_README.md))
- Django 5.1 & Python 3.12

## Table of Contents
* **[Installation](#installation)**
  * [Pip](#pip)
  * [Docker](#docker)
* [Next Steps](#next-steps)
* [Contributing](#contributing)
* [Support](#support)
* [License](#license)

## 📖 Installation
Healthy Meals can be installed via Pip or Docker. To start, clone the repo to your local computer and change into the proper directory.

```
$ git clone https://github.com/tayloredwebsites/healthy_meals.git
$ cd healthy_meals
```

### Pip
You can use [pip](https://pypi.org/project/pip/) to create a fresh virtual environment on either Windows or macOS.

```
# On Windows
$ python -m venv .venv
$ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
$ .venv\Scripts\Activate.ps1
(.venv) $

# On macOS
$ python -m venv .venv
$ source .venv/bin/activate
(.venv) $
```

Then install all packages hosted in `requirements.txt` and run `migrate` to configure the initial database. The command `createsuperuser` will create a new superuser account for accessing the admin. Execute the `runserver` commandt o start up the local server.

```
(.venv) $ pip install -r requirements.txt
(.venv) $ python manage.py migrate
(.venv) $ python manage.py createsuperuser
(.venv) $ python manage.py runserver
# Load the site at http://127.0.0.1:8000 or http://127.0.0.1:8000/admin for the admin
```

### Docker

## Next Steps

## 🤝 Contributing

## ⭐️ Support

Give a ⭐️  if this project helped you!

## License

Copyright (C) 2024 David A. Taylor of Taylored Web Sites (tayloredwebsites.com)
Licensed under [AGPL-3.0-only](https://opensource.org/license/agpl-v3/)

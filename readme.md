# Agency Justo's

Challenge.


### Tech Stack

* Django 3.2.3
* Django Rest Framework
* Python 3.9
* Postgres 13.0
* Virtualenv
* Git
* Github
* [Git Flow](https://www.atlassian.com/es/git/tutorials/comparing-workflows/gitflow-workflow)

### Libraries

* pre-commit = https://github.com/pre-commit/pre-commit
* Coverage = https://github.com/nedbat/coveragepy
* Black = https://github.com/psf/black
* Pytest = https://docs.pytest.org/en/stable/
* Psycopg2-binary = https://www.psycopg.org/
* Flake8 = https://github.com/PyCQA/flake8
* Pudb = https://pypi.org/project/pudb/
* Python-decouple = https://pypi.org/project/python-decouple/

### Tools
* Lucichart = https://www.lucidchart.com/pages/es




## Documentation

### ERD (Entity Relationship Diagram)

![Logo](https://i.imgur.com/lc7RONo.png)


## Run Locally

Create virtualenviroment
```bash
  virtualenv -p python3.9 .env
```

Activate virtualenviroment
```bash
  source .env/bin/activate
```

Clone the project

```bash
  https://github.com/IvanMSP/justo-agency.git
```

Install requirements from txt file
```bash
  pip install -r requirements/develop.txt
```

Create database on Postgres
```bash

    CREATE DATABASE database_name;

    # Create User
    CREATE USER user WITH PASSWORD 'passswordstrong';

    # Users settings
    ALTER ROLE user SET client_encoding TO 'utf8';
    ALTER ROLE user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE user SET timezone TO 'UTC';

    # Grant priveliges
    GRANT ALL PRIVILEGES ON DATABASE database_name TO user;
```

Go to the project directory and create file .env for enviroments variables
```bash
   touch .env

   # Added the next variables:
   NAMEDB
   USERDB
   PASSWORDDB
   HOST
   PORT
   SECRET_KEY
   DEBUG
   SETTINGS_MODULE
```

Run Migrations
```bash
  python manage.py migrate
```

Create data initial for the project.
```bash
  python manage.py loaddata data_initial.json
```

Ready for run project
```bash
  python manage.py runserver
```

## Pre-Commit

Precommit was configured with black and flake-8, respectively a code formatter and a linter, pre-commit checks your code every time you commit.

### (.pre-commit-config.yaml)

  ```bash
  repos:
  -   repo: https://github.com/ambv/black
      rev: 20.8b1
      hooks:
      - id: black
        language_version: python3.9.1
  -   repo: https://gitlab.com/pycqa/flake8
      rev: 3.9.0
      hooks:
      - id: flake8

  # Optional hook. Check dependencies are safe
  -   repo: https://github.com/Lucas-C/pre-commit-hooks-safety
      rev: v1.2.1
      hooks:
      -   id: python-safety-dependencies-check
  ```

### File configuration for Black and Flake8
```bash
  black.toml

  .flake8
```

### Install pre-commit into project

  ```bash
  pre-commit install
  ```

## Next Steps

## Deploy

### Tools

* Google Cloud Platform
* VM with Debian SO
* Cloud Storage for storage media files from project
* VM with Postgres 13

* Nginx
* Supervisor
* Gunicorn

### Architecture

![Architecture](https://i.imgur.com/gc9xnHc.png)


### Notes:

In learning process:
CI Integration with Jenkins, for ease deploy. :)
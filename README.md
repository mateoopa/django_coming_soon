# Coming Soon - Django Application

## Prerequisites
- [Python](https://www.python.org/) (with [pip](https://pypi.org/project/pip/) and [virtualenv](https://virtualenv.pypa.io/)) installed on your development machine. If you do not have Python, visit the previous link for download options.

## Create a virtual environment

- In your command-line interface (CLI), navigate to this directory and run the following command to create a virtual environment.

    ```Shell
    python -m virtualenv venv
    ```

## Activate virtual environment

- In your command-line interface (CLI), navigate to "venv/scripts" directory and run the following command to activate it.

    ```Shell
    activate
    ```
    
## Install requirements

- Run the following command to install requirements.

    ```Shell
    pip install -r requirements.txt
    ```
    
## Perform DB migrations

- Run the following commands in your CLI to run perform the DB migrations.

    ```Shell
    python manage.py makemigrations
    python manage.py migrate
    ```

## Insert data from json
- Run the following command in your CLI to create the logs user in the DB.
    ```Shell
    python manage.py loaddata data.json
    ```

## Create groups
- Run the following command in your CLI to create the default groups in the DB.
    ```Shell
    python manage.py initgroups
    ```

## Run the application

- Run the following commands in your CLI to run the application.

    ```Shell
    python manage.py runserver
    ```

# Other commands

## Inspect groups
- Run the following command in your CLI to get the existing groups in the DB and their permissions.
    ```Shell
    python manage.py inspectgroups
    ```

## Inspect a DB

- Run the following commands in your CLI to inspect a specific database.

    ```Shell
    python manage.py inspectdb --database default> inspect_models.py
    ```

## Migrate a DB

- Run the following commands in your CLI to migrate a specific database.

    ```Shell
    python manage.py migrate --database=<default>
    ```

## No such table Error

- Run the following commands in your CLI when having "No such table Error".

    ```Shell
    python manage.py makemigrations <app_label>
    python manage.py migrate --run-syncdb
    ```
# Playing with Flask and uWSGI

## Prerequisites

Get yourself a virtual environment with Flask.

virtualenv venv
source venv/bin/activate
pip install flask
pip install uwsgi

## Features

* store user configuration in conf/<user>.cnf files
* work in Flask debug and uWSGI

## Using it with Flask

## Using it with gunicorn

gunicorn --bind=0.0.0.0 --workers=4 startup:app

## Using it with uWSGI


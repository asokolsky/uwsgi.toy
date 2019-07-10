# Playing with Flask and uWSGI

This is a work in progress and all the features mentioned below
are delivered yet.

## Prerequisites

Get yourself a virtual environment with Flask. Then:

```bash
virtualenv venv
source venv/bin/activate
pip install flask
pip install uwsgi
```

## Features

* store user configuration in conf/`<user>`.cnf files
* work in Flask debug and uWSGI and gunicorn

## Using it with Flask debug server

`python run`

## Using it with gunicorn

`gunicorn --bind=0.0.0.0 --workers=4 startup:app`

## Using it with uWSGI



#
#
#
import logging
import os
from flask import Flask, request, current_app
from . import app



@app.route('/')
def hello_world():
    return 'Hello, World!'

#
#
#
import logging
import os
from flask import Flask, request, current_app

app = None


def create_app(config):
    global app
    path_to_conf = os.path.abspath(os.path.join( __file__, '../../conf' ))
    print('path_to_conf:' + path_to_conf)
    app = Flask( 
        __name__, 
        instance_path=path_to_conf,
        instance_relative_config=True)
    #with app.open_instance_resource( config ) as f:
    #    config = f.read()
    #    pass

    app.config.from_pyfile(config)
    return app
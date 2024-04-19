#!/usr/bin/python3
from flask import Flask
from models import storage
from api.v1.views import app_views
import os

"""
This new app module to manage application
this module will create a Flask app called app
This module will define @app.teardown_appcontext
by close_app methode
and will register to app_views blueprint"""


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_app(Exception):
    """
    closin app and will close the Flask app
    this method accept an exception
    it closes the store when it is executed
    """
    storage.close()


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = os.getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)

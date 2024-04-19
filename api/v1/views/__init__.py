#!/usr/bin/python3
from flask import Blueprint
"""
This is a __init__ file to initialize import
This will create app_views blueprint
this will import every thing within index
"""


app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views import index

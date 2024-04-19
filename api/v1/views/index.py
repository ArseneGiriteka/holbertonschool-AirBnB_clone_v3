#!/usr/bin/python3
from api.v1.views import app_views
from flask import jsonify
"""index file that defines routes"""


@app_views.route('/status')
def app_view_ok():
    """app_view_ok method defines the /status route"""
    return jsonify({"status": "Ok"})

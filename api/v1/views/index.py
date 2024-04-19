#!/usr/bin/python3
"""
index file that defines routes
this will import app_views
this will import jsonify to jsonify the return dictionary
this will define /status route
this will add new  method app_view_ok
"""


from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def app_view_ok():
    """
    app_view_ok method defines the /status route
    this methode is called app_view and will return a
    json text formated
    it will always return {"status": "Ok"}
    """
    return jsonify({"status": "Ok"})

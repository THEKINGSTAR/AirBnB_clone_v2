#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""
from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    lsit all states
    """
    state_list = storage.all("State").values()
    return (render_template("7-states_list.html", states=state_list))


@app.teardown_appcontext
def close_db(exception=None):
    """
    After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

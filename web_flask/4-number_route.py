#!/usr/bin/python3
"""
Script that starts a Flask web application:
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """display “Hello HBNB!”"""
    return ("Hello HBNB!")


@app.route("/hbnb", methods=['GET'], strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return ("HBNB")


@app.route("/c/<text>", methods=['GET'], strict_slashes=False)
def txt(text):
    """display “C ”, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return (f"C {escape(text)}")


@app.route("/python/", methods=['GET'], strict_slashes=False)
@app.route("/python/<text>", methods=['GET'], strict_slashes=False)
def Python(text="is cool"):
    """display “Python ”, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return (f"Python {escape(text)}")


@app.route("/number/<int:n>", methods=['GET'], strict_slashes=False)
def Number(n):
    """display “n is a number” only if n is an integer"""
    try:
        n = int(n)
        return (f"{escape(n)} is a number")
    except exeption:
        return (None)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

#!/usr/bin/env python3
""" Basic Babel setup """
from flask import Flask, render_template
from typing import Any
from flask_babel import Babel


class Config(object):
    """ Language config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index() -> Any:
    """ renders templates """
    return (render_template('1-index.html'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

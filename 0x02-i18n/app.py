#!/usr/bin/env python3
""" Basic Babel Setup """
from flask import Flask, render_template, request, g
from typing import Any, Dict
from flask_babel import Babel
from datetime import datetime
import locale
from pytz import timezone
import pytz.exceptions


class Config(object):
    """ Language config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
    """ returns a user dict """
    id = request.args.get('login_as')
    if not id:
        return None
    id = int(id)
    if id not in users:
        return None
    return users[id]


@app.before_request
def before_request():
    """ first function to run """
    current_user = get_user()
    g.user = current_user
    time_now = pytz.utc.localize(datetime.utcnow())
    time = time_now.astimezone(timezone(get_timezone()))
    locale.setlocale(locale.LC_TIME, (get_locale(), 'UTF-8'))
    time_format = "%b %d, %Y %I:%M:%S %p"
    g.time = time.strftime(time_format)


@babel.localeselector
def get_locale():
    """ returns locale lang """
    url_locale = request.args.get('locale')
    if url_locale:
        locale = url_locale
    elif g.user:
        locale = g.user.get('locale', '')
    elif request.headers.get('locale', ''):
        locale = request.headers.get('locale', '')
    else:
        locale = None
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """ gets the timezone """
    url_tz = request.args.get('timezone')
    if url_tz:
        tz = url_tz
    elif g.user:
        tz = g.user.get('timezone', '')
    elif request.headers.get('timezone', ''):
        tz = request.headers.get('timezone', '')
    else:
        tz = None
    if tz:
        try:
            return pytz.timezone(tz).zone
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index() -> Any:
    """ renders templates """
    return (render_template('7-index.html'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

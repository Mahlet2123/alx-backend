#!/usr/bin/env python3
""" 0-app module """
from flask import Flask, render_template, g
from flask_babel import Babel, request


app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABLE_DEFAULT_LOCALE = "en"
    BABLE_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False

babel = Babel(app)


@babel.localeselector
def get_locale():
    """ Select best language """
    # detect if the incoming request contains locale argument
    request_locale = request.args.get('locale')

    if request_locale in Config.LANGUAGES:
        return request_locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user():
    """
    returns a user dictionary or None if the ID cannot
    be found or if login_as was not passed.
    """
    request_user = request.args.get('login_as')

    if request_user:
        return users.get(int(request_user))
    return None


@app.before_request
def before_request():
    """
    use get_user to find a user if any,
    and set it as a global on flask.g.user
    """
    user = get_user()
    g.user = user

@app.route("/")
def index():
    """ '/' route """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="5000",
            debug=True)

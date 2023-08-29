#!/usr/bin/env python3
""" 0-app module """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABLE_DEFAULT_LOCALE = "en"
    BABLE_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

babel = Babel(app)


@app.route("/", strict_slashes = False)
def index() -> str:
    """ '/' route """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",
            port="5000",
            debug=True)

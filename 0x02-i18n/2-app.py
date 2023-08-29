#!/usr/bin/env python3
""" 0-app module """
from flask import Flask, render_template
from flask import Bable, request


app = Flask(__name__)

class Config:
    LANGUAGES = ["en", "fr"]
    BABLE_DEFAULT_LOCALE = "en"
    BABLE_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

bable = Bable(app)

@bable.localeselector
def get_locale():
    """ Select best language """
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route("/")
def index():
    """ '/' route """
    return render_template("./templates/2-index.html")


if __name__ == "__main__":
    app.run()

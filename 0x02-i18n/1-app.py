#!/usr/bin/env python3
""" 0-app module """
from flask import Flask, render_template
from flask import Bable


app = Flask(__name__)

class Config:
    LANGUAGES = ["en", "fr"]
    BABLE_DEFAULT_LOCALE = "en"
    BABLE_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

bable = Bable(app)

@app.route("/")
def index():
    """ '/' route """
    return render_template("./templates/1-index.html")


if __name__ == "__main__":
    app.run()

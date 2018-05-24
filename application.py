from flask import Flask, flash, redirect, render_template, request, session, url_for
from helpers import *

# configure application
app = Flask(__name__)

@app.route("/" , methods=["GET", "POST"])
@app.route("/index.html" , methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return render_template("index.html")

    else:
        return render_template("index.html")


@app.route("/notes.html")
def notes():
    return render_template("notes.html")


if __name__ == '__main__':
    app.run(debug=True)
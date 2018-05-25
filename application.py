from flask import Flask, flash, redirect, render_template, request, session, url_for

# configure application
app = Flask(__name__)

@app.route("/" , methods=["GET", "POST"])
@app.route("/index.html" , methods=["GET", "POST"])
def index():
    if request.method == "POST":

        if not request.form.get("note"):
            return render_template("error.html")


        return render_template("notes.html")

    else:
        return render_template("index.html")


@app.route("/notes.html")
def notes():
    return render_template("notes.html")


if __name__ == '__main__':
    app.run(debug=True)
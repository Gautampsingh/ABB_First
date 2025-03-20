
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1> Hello World </h1>"

@app.route("/<username>")
def user(username):
    return f"<h3> Greetings {username}, Welcome to Flask Programming... </h3>"

@app.route("/admin")
def admin():
    # return redirect(url_for("home"))
    return redirect(url_for("user", username="Root"))

if __name__ == '__main__':
    # app.run(debug=True, use_reloader=True, port=7000)
    app.run(debug=True, use_reloader=True)



from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "123@hello"
flag = False

@app.route("/")
def home():
    return render_template("index03.html", uname='Joseph')

@app.route("/login", methods=['GET', 'POST'])
def login():
    global flag
    if request.method == 'POST':
        user = request.form['nm']
        flag = True
        return redirect(url_for("user", usr=user))
    else:
        flag = False
        if flag == False:
            flash("You have used GET Method......")
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    global flag
    if flag:
        flash("You have used the POST method......")
    return render_template("result.html", usr=usr)

@app.route("/index")
def index():
    return render_template("index02.html", uname="Tyson", content='Fruits available in all seasons',
                           fruits=['Apple', 'Orange', 'Grapes', 'Banana', 'Pineapple', 'Strawberry', 'Watermelon',
                                   'Mango', 'Blueberry'])

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

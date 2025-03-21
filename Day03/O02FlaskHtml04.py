
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index03.html", uname="Mike Tyson")

@app.route("/index")
def index():
    return render_template("index02.html", uname="Tyson", content='Fruits available in all seasons',
                           fruits=['Apple', 'Orange', 'Grapes', 'Banana', 'Pineapple', 'Strawberry', 'Watermelon',
                                   'Mango', 'Blueberry'])
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)



from flask import Flask, render_template, make_response,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index02.html", uname="Mike Tyson", content='Fruits available in all seasons', fruits=['Apple', 'Orange', 'Grapes', 'Banana', 'Pineapple', 'Strawberry', 'Watermelon', 'Mango', 'Blueberry'])

@app.route("/set_cookie")
def set_cookie():
    resp = make_response("Success")
    resp.set_cookie("Prod1", "Pepsi")
    resp.set_cookie("Prod2", "Tropicana")
    return resp

@app.route("/get_cookie")
def get_cookie():
    prd1 = request.cookies.get('Prod1')
    prd2 = request.cookies.get('Prod2')
    if prd1 == None:
        prd1 = "Cookie Deleted"
    elif prd2 == None:
        prd2 = "Cookie Deleted"
    return f"<h2> Fist Cookie : {prd1} <br> Second Cookie : {prd2} </h2>"

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)


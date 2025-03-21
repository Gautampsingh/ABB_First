
from flask import Flask, request, flash, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "abcd"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/students'
# will not create a database if a proper db like mysql is used, it only creates a Table

db = SQLAlchemy(app)

class Students(db.Model):
    studid = db.Column('student_id', db.Integer, primary_key = True)
    sname = db.Column(db.String(50))
    stdcls = db.Column(db.String(50))
    city = db.Column(db.String(50))

    def __init__(self, name, scls, city):
        self.sname = name
        self.stdcls = scls
        self.city = city

@app.route("/")
def show_all():
    return render_template("show_all.html", students=Students.query.all())


@app.route("/new", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['sname'] or not request.form['scls'] or not request.form['city']:
            flash("Please enter all the fields", "error")
        else:
            student = Students(request.form['sname'], request.form['scls'], request.form['city'])
            db.session.add(student)
            db.session.commit()

            flash("Record added successfully into the database......")
            return redirect(url_for("show_all"))
    return render_template("new.html")


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(debug=True, use_reloader=True)
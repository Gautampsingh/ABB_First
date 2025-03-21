
from flask import Flask, request, jsonify, make_response, request, render_template, session, flash
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)

app.config['SECRET_KEY'] = '2927ce7338ba42a4b52f15abbbd658e6'


def token_required(func):
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401

        try:

            data = jwt.decode(token, app.config['SECRET_KEY'])

        except:
            return jsonify({'Message': 'Invalid token'}), 403
        return func(*args, **kwargs)

    return decorated


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login1.html')
    else:
        return 'logged in currently'


@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard !  '


# Login page


@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True

        token = jwt.encode({
            'user': request.form['username'],
            # don't foget to wrap it in str function, otherwise it won't work [ i struggled with this one! ]
            'expiration': str(datetime.utcnow() + timedelta(seconds=60))
        },
            app.config['SECRET_KEY'])
        return jsonify({'token': token})
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})


if __name__ == "__main__":
    app.run(debug=True)

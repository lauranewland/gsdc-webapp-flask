from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud
from jinja2 import StrictUndefined

# Creates an instance of the Flask
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Renders Homepage"""

    return render_template('homepage.html')


@app.route('/users', methods=['POST'])
def register_user():
    """Create a new user.

    .. note::
        Checks if the user email is already in the database.
        If yes, a flash message will note the email already exists
        if not, the user will be created
    """

    fname = request.form.get('fname')
    lname = request.form.get('lname')
    email = request.form.get('email')

    user = crud.get_user_by_email(email)

    # Checks if a us
    if user:
        flash('Email Already Exists.')
    else:
        crud.create_user(fname, lname, email)
        flash('Membership Application Submitted.')

    return redirect('/signup')


@app.route('/signup')
def signup_page():
    """Renders Membership Signup Page"""

    return render_template('membership_signup.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

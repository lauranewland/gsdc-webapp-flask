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
    address = request.form.get('address')
    city = request.form.get('city')
    zip_code = request.form.get('zip_code')
    phone = request.form.get('phone')
    pref_communication = request.form.get('pref_communication')
    print_permissions = request.form.get('print_permissions')
    member_type = request.form.get('member_type')
    # password = request.form.get('password')
    other_orgs = request.form.get('other_orgs')
    num_of_gsd = request.form.get('num_of_gsd')
    num_breedings = request.form.get('num_breedings')

    user = crud.get_user_by_email(email)

    if user:
        flash('Email Already Exists.')
    else:
        # crud.create_user(fname, lname, email)

        crud.create_user(fname, lname, email, address, city, zip_code, phone, pref_communication, print_permissions,
                         member_type, other_orgs, num_of_gsd, num_breedings)

        flash('Membership Application Submitted.')

    return redirect('/signup')


@app.route('/signup')
def signup_page():
    """Renders Membership Signup Page"""

    return render_template('membership_signup.html')


# @app.route('/users/{user_id}/interest/', methods=['POST'])
# def create_interest_for_user():
#     """Returns a newly created item"""
#     pass


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

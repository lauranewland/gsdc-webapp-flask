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
    print_permissions = bool(request.form.get('print_permissions'))
    member_type = request.form.get('member_type')
    # password = request.form.get('password')
    other_orgs = request.form.get('other_orgs')
    num_of_gsd = request.form.get('num_of_gsd')
    num_breedings = request.form.get('num_breedings')

    obedience = bool(request.form.get('obedience'))
    rally = bool(request.form.get('rally'))
    conformation = bool(request.form.get('conformation'))
    agility = bool(request.form.get('agility'))
    herding = bool(request.form.get('herding'))
    scentwork = bool(request.form.get('scentwork'))
    fun_match = bool(request.form.get('fun_match'))
    shep_o_gram = bool(request.form.get('shep_o_gram'))
    training = bool(request.form.get('training'))
    hospitality = bool(request.form.get('hospitality'))
    fundraising = bool(request.form.get('fundraising'))
    gsd_fun_day = bool(request.form.get('gsd_fun_day'))
    demo_mn_fair = bool(request.form.get('demo_mn_fair'))
    annual_banquet = bool(request.form.get('annual_banquet'))
    breeding = bool(request.form.get('breeding'))
    other = request.form.get('other')

    user = crud.get_user_by_email(email)

    if user:
        flash('Email Already Exists.')
        return redirect('/signup')
    else:

        new_user = crud.create_user(fname, lname, email, address, city, zip_code, phone, pref_communication,
                                    print_permissions,
                                    member_type, other_orgs, num_of_gsd, num_breedings)

        crud.create_user_interest(new_user.user_id, obedience, rally, conformation, agility, herding, scentwork,
                                  fun_match, shep_o_gram,
                                  training, hospitality, fundraising, gsd_fun_day, demo_mn_fair, annual_banquet,
                                  breeding, other)

        flash('Membership Application Submitted.')

    return redirect('/')


@app.route('/signup')
def signup_page():
    """Renders Membership Signup Page"""

    return render_template('membership_signup.html')


@app.route('/user')
def all_users():
    user = crud.get_all_users()
    return render_template('all_users.html', user=user)


@app.route('/search', methods=["GET", "POST"])
def search_user_by_name():
    """Takes in a request from Search.html and returns results"""

    # Takes in the search input
    user_input = request.form.get('memberInput')

    # Queries the users input against the database
    user = crud.get_user(user_input)

    # Passes the query results back to Search.html
    return render_template('search.html', user=user)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
from werkzeug.security import check_password_hash
from model import connect_to_db, Users
from jinja2 import StrictUndefined
import crud
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

# Creates an instance of Flask
app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Creates an instance of Flask LoginManager
login_manager = LoginManager()
login_manager.login_view = 'app.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


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
    password = request.form.get('password')
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

    # Queries database on the email address and stores all data in user
    user = crud.get_user_by_email(email)

    # Checks if a user account has been found in the database
    if user:
        # If so, flash a message that the email already exists
        flash('Email Already Exists.')
        return redirect('/signup')

    # Otherwise add a new user and their interest to the database
    else:
        new_user = crud.create_user(fname, lname, email, address, city, zip_code, phone, pref_communication,
                                    print_permissions, member_type, password, other_orgs, num_of_gsd, num_breedings)

        crud.create_user_interest(new_user.user_id, obedience, rally, conformation, agility, herding, scentwork,
                                  fun_match, shep_o_gram,training, hospitality, fundraising, gsd_fun_day, demo_mn_fair,
                                  annual_banquet, breeding, other)

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
def search_database():
    """Takes in a request from Search.html and returns results"""

    # Takes in the search input
    user_input = request.form.get('meminput')
    print(user_input)

    users = crud.get_user_interest(user_input)
    print(users)

    if len(users) != 0:
        return render_template('search.html', name=current_user.fname, users=users)
    else:
        users = crud.get_user(user_input)
        print(users)
        return render_template('search.html', name=current_user.fname, users=users)


@app.route('/login')
def login():

    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login_post():
    """Takes in Users input and checks password & email matches the user in the database
        If a match, a user login session is created and the user is routed to the login_landing page"""

    # Takes in the users input
    email = request.form.get('useremail')
    print(email)
    password = request.form.get('upassword')
    print(password)
    remember = True if request.form.get('remember') else False

    # Sets the users variable to an empty list to be a place holder for the login_landing page
    users = []
    try:
        # Queries database on the email address and stores all data in user
        user = crud.get_user_by_email(email)
        print(user)
        # Checks if password and email the user input matches the database
        if check_password_hash(user.password, password):
            # Creates Session for the logged in user
            login_user(user, remember=remember)
            flash('Successful Login')

        # If users password does not match flash message
        else:
            flash('Password Incorrect')
            return redirect('/login')

    # If users email does not match flash message
    except AttributeError:
        flash('Email not found')
        return redirect('/login')

    # Renders the login_landing page and passes the logged in users first name
    return render_template('login_landing.html', name=current_user.fname, users=users)


@app.route('/login_landing')
@login_required
def login_landing():
    """Renders Login Landing Page"""
    return render_template('login_landing.html', name=current_user.fname)


@app.route('/isLoggedIn')
def logged_in():
    """AJAX backed for log"""
    return jsonify(current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')


# @app.route('/interest', methods=["GET", "POST"])
# def search_user_interest():
#     """Takes in a request from Search.html and returns results"""
#
#     # Takes in the search input
#     user_input = request.form.get('memberInput')
#     print(user_input)
#
#     # Queries the users input against the database
#     intresults = crud.get_user_interest(user_input)
#     print(intresults)
#
#     # Passes the query results back to Search.html
#     return render_template('interest.html', intresults=intresults)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)

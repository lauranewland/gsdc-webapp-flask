import sqlalchemy
from flask import flash

from model import Users, Interest, db, connect_to_db
from werkzeug.security import generate_password_hash


def create_user(fname, lname, email, address, city, zip_code, phone, pref_communication, print_permissions,
                member_type, password, other_orgs, num_of_gsd, num_breedings):
    user = Users(fname=fname, lname=lname, email=email, address=address, city=city, zip_code=zip_code, phone=phone,
                 pref_communication=pref_communication, print_permissions=print_permissions, member_type=member_type,
                 password=generate_password_hash(password, method='sha256'), other_orgs=other_orgs,
                 num_of_gsd=num_of_gsd, num_breedings=num_breedings)

    # Adds user interest to the database session
    db.session.add(user)

    # Commits user interest to the database
    db.session.commit()

    # Refreshes the database instances
    db.session.refresh(user)

    return user


def get_user_by_email(email):
    """Queries a user by email"""

    return Users.query.filter(Users.email == email).first()


def get_all_users():
    """Queries and returns all users"""
    return Users.query.all()


def get_user(user_input):
    """Queries and returns a user"""
    return Users.query.filter(Users.fname == user_input).all()


def create_user_interest(user_id, obedience, rally, conformation, agility, herding, scentwork, fun_match, shep_o_gram,
                         training, hospitality, fundraising, gsd_fun_day, demo_mn_fair,
                         annual_banquet, breeding, other):
    """Creates a user interest"""

    interest = Interest(user_id=user_id, obedience=obedience, rally=rally, conformation=conformation, agility=agility,
                        herding=herding, scentwork=scentwork, fun_match=fun_match, shep_o_gram=shep_o_gram,
                        training=training, hospitality=hospitality, fundraising=fundraising, gsd_fun_day=gsd_fun_day,
                        demo_mn_fair=demo_mn_fair, annual_banquet=annual_banquet, breeding=breeding, other=other)

    # Adds user interest to the database session
    db.session.add(interest)

    # Commits user interest to the database
    db.session.commit()

    # Refreshes the database instances
    db.session.refresh(interest)

    return interest


def get_user_interest(user_input):
    """Queries an interest and returns members associated with it"""

    try:
        if user_input is None:
            """User_input is going to be nothing when the page first renders 
                this statement returns an empty list"""
            return []
        else:
            query = ("SELECT * FROM users WHERE user_id IN "
                 f"(SELECT user_id FROM interests WHERE {user_input} = true)")

            # Executes the Query
            db_cursor = db.session.execute(query)
            return db_cursor.fetchall()
    except sqlalchemy.exc.OperationalError:

        return []


if __name__ == '__main__':
    from server import app

    connect_to_db(app)

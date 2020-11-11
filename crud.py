from model import Users, db


def create_user(fname, lname, email):
    """Create and return a new user."""
    user = Users(fname=fname, lname=lname, email=email)

    db.session.add(user)
    db.session.commit()

    return user

    """This function will be implemented later"""
# def create_user(fname, lname, email, address, city, zip_code, phone, pref_communication, print_permissions,
    #   password, member_type, member_standing, other_orgs, num_of_gsd, num_breedings):

    # user = Users(fname=fname, lname=lname, email=email, address=address, city=city, zip_code=zip_code, phone=phone,
    # pref_communication=pref_communication, print_permissions=print_permissions, password=password,
    # member_type=member_type, member_standing=member_standing, other_orgs=other_orgs, num_of_gsd=num_of_gsd,
    # num_breedings=num_breedings)

    # db.session.add(user)
    # db.session.commit()

    # return user


def get_user_by_email(email):
    """Queries a user by email"""

    return Users.query.filter(Users.email == email).first()

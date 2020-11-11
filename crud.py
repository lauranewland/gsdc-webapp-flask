from model import Users, Interest, db


def create_user(fname, lname, email, address, city, zip_code, phone, pref_communication, print_permissions,
                member_type, other_orgs, num_of_gsd, num_breedings):
    user = Users(fname=fname, lname=lname, email=email, address=address, city=city, zip_code=zip_code, phone=phone,
                 pref_communication=pref_communication, print_permissions=print_permissions, member_type=member_type,
                 other_orgs=other_orgs, num_of_gsd=num_of_gsd, num_breedings=num_breedings)

    db.session.add(user)
    db.session.commit()

    return user


def get_user_by_email(email):
    """Queries a user by email"""

    return Users.query.filter(Users.email == email).first()


def create_user_interest(obedience, rally, conformation, agility, herding, scentwork, fun_match, shep_o_gram,
                         training, hospitality, fundraising, gsd_fun_day, demo_mn_fair, annual_banquet, breeding,
                         other):
    """Creates a user interest"""

    interest = Interest(obedience=obedience, rally=rally, conformation=conformation, agility=agility,
                        herding=herding, scentwork=scentwork, fun_match=fun_match, shep_o_gram=shep_o_gram,
                        training=training, hospitality=hospitality, fundraising=fundraising, gsd_fun_day=gsd_fun_day,
                        demo_mn_fair=demo_mn_fair, annual_banquet=annual_banquet, breeding=breeding, other=other)

    # Adds user interest to the database session
    db.add(interest)

    # Commits user interest to the database
    db.commit()

    return interest

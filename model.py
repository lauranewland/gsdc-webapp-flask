from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_to_db(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///./gsdc.db"

    db.app = flask_app
    db.init_app(flask_app)

    # Creates database tables
    db.create_all()
    print('Connected to the db!')


class Users(db.Model):
    """Data Model for a User"""

    # Creates a table of users
    __tablename__ = 'users'

    # Defines the Schema for the users table
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    address = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    zip_code = db.Column(db.String(10), nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    pref_communication = db.Column(db.String(50), nullable=True)
    print_permissions = db.Column(db.Boolean, nullable=True)
    password = db.Column(db.String(50), nullable=True)
    member_type = db.Column(db.String(100), nullable=True)
    member_standing = db.Column(db.String(25), default='Good')
    other_orgs = db.Column(db.Text)
    num_of_gsd = db.Column(db.Integer)
    num_breedings = db.Column(db.Integer)

    # app_date = db.Column(Date)
    # # co_app_fname = db.Column(db.String(50))
    # # co_app_lname = db.Column(db.String(50))
    # # co_app_email = db.Column(db.String(100))

    def __repr__(self):
        return f'<user_id={self.user_id}, fname={self.fname}, lname={self.lname}>'


class Interest(db.Model):
    """Data Model for User Interest"""

    # Creates a table of user interests
    __tablename__ = 'interests'

    # Defines the Schema for the users interest table
    interest_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    obedience = db.Column(db.Boolean)
    rally = db.Column(db.Boolean)
    conformation = db.Column(db.Boolean)
    agility = db.Column(db.Boolean)
    herding = db.Column(db.Boolean)
    scentwork = db.Column(db.Boolean)
    fun_match = db.Column(db.Boolean)
    shep_o_gram = db.Column(db.Boolean)
    training = db.Column(db.Boolean)
    hospitality = db.Column(db.Boolean)
    fundraising = db.Column(db.Boolean)
    gsd_fun_day = db.Column(db.Boolean)
    demo_mn_fair = db.Column(db.Boolean)
    annual_banquet = db.Column(db.Boolean)
    breeding = db.Column(db.Boolean)
    other = db.Column(db.String(100))

    def __repr__(self):
        return f'<interest_id={self.interest_id}, obedience={self.obedience}, training={self.training}>'

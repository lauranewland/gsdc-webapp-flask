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
    # address = db.Column(db.String(100), nullable=False)
    # city = db.Column(db.String(50), nullable=False)
    # zip_code = db.Column(db.String(10), nullable=False)
    # phone = db.Column(db.String(15), nullable=False)
    # pref_communication = db.Column(db.String(50), nullable=False)
    # print_permissions = db.Column(db.Boolean, nullable=False)
    # password = db.Column(db.String(50), nullable=False)
    # member_type = db.Column(db.String(100), nullable=False)
    # member_standing = db.Column(db.String(25), nullable=False)
    # other_orgs = db.Column(db.Text)
    # num_of_gsd = db.Column(db.Integer)
    # num_breedings = db.Column(db.Integer)
    # # app_date = db.Column(Date)
    # # co_app_fname = db.Column(db.String(50))
    # # co_app_lname = db.Column(db.String(50))
    # # co_app_email = db.Column(db.String(100))

    # Add Relationship to Interest Table
    # interest = relationship('Interest', back_populates='user')

    def __repr__(self):
        return f'<user_id={self.user_id}, fname={self.fname}, lname={self.lname}>'





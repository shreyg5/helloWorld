from app import app, db
from models import Major, User
from werkzeug.security import generate_password_hash

# Activate the application context
with app.app_context():
    # Drop existing tables and create new ones
    db.drop_all()
    db.create_all()

    # Initial loading of majors
    majors = ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management', \
              'Operations Management & Business Analytics', 'Supply Chain Management']
    for each_major in majors:
        # Insert each major into the database
        print(f'{each_major} inserted into major')
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Initial users information
    users = [
        {'username': 'shreyg', 'email': 'shreyg@umd.edu', 'first_name':'Shreya', 'last_name':'Gupta',
            'password': generate_password_hash('shreyagupta', method='pbkdf2:sha256'), 'role':'STUDENT'},
        {'username': 'manager', 'email': 'manager@umd.edu', 'first_name':'Joe', 'last_name':'King',
            'password': generate_password_hash('managerpw', method='pbkdf2:sha256'), 'role':'MANAGER'},
        {'username': 'admin', 'email': 'admin@umd.edu', 'first_name':'Crystal', 'last_name':'Ball',
            'password': generate_password_hash('adminpw', method='pbkdf2:sha256'), 'role':'ADMIN'}
    ]

    for each_user in users:
        # Insert each user into the database
        print(f'{each_user["username"]} inserted into user')
        a_user = User(username=each_user["username"], email=each_user["email"], first_name=each_user["first_name"],
                      last_name=each_user["last_name"], password=each_user["password"], role=each_user["role"])
        db.session.add(a_user)
        db.session.commit()
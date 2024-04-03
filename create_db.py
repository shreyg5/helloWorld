from app import app, db
from models import Student, Major
import datetime as dt

# Establish app context
with app.app_context():
    # Drop existing tables and create new ones
    db.drop_all()
    db.create_all()

    # Populate Major table
    for each_major in ['Accounting', 'Finance', 'Information Systems', 'International Business', 'Management',
                       'Operations Management & Business Analytics', 'Supply Chain Management']:
        a_major = Major(major=each_major)
        db.session.add(a_major)
        db.session.commit()

    # Populate Student table
    for each_student in [
        {'student_id': '1', 'first_name': 'Robert', 'last_name':'Smith', 'major_id':3, 'email': 'rsmith@umd.edu',
            'birth_date': dt.date(2007, 6, 1), 'is_honors':1},
        {'student_id': '2', 'first_name': 'Leo', 'last_name': 'Van Munching', 'major_id':6, 'email': 'lmunching@umd.edu',
         'birth_date': dt.date(2008, 3, 24), 'is_honors': 0},
    ]:
        a_student = Student(first_name=each_student["first_name"], last_name=each_student["last_name"],
                            major_id=each_student["major_id"], email=each_student["email"],
                            birth_date=each_student["birth_date"], is_honors=each_student["is_honors"])
        db.session.add(a_student)
        db.session.commit()





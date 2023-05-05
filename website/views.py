#this file stores the routes for all static pages on website. 
#home, about us, etc.

from flask import Blueprint
from flask import render_template

from sql_scripts import get_all_tutors, get_name, get_age

views = Blueprint('views', __name__)

#defines route, in this case home = / cuz it goes nowhere. 
@views.route('/')
def home():
    return render_template("home.html")

@views.route('/about_us')
def about_us():
    return render_template("aboutUs.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")
@views.route('/tutors')
def tutors():
    db_raw = get_all_tutors()
    print(db_raw)

    j=0
    for i in db_raw:
        j = j+1

    #{name, age, subject, description, picture}

    #taking this in good faith
    new_data = [ [0 for i in range(5)]for i in range(j)]

    j=0
    for i in db_raw:
        #name
        new_data[j][0] = get_name(db_raw[j][0])
        #age
        new_data[j][1] = get_age(db_raw[j][0])
        #subject
        new_data[j][2] = db_raw[j][2]
        #description
        new_data[j][3] = db_raw[j][1]
        #picture
        new_data[j][4] = db_raw[j][3]
        j = j+1

    return render_template("teachers.html", data=new_data)
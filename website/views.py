#this file stores the routes for all static pages on website. 
#home, about us, etc.

from flask import Blueprint
from flask import render_template
from flask import request


from sql_scripts import get_all_tutor_info, get_searched_tutors

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
    new_data = get_all_tutor_info()
    return render_template("teachers.html", data=new_data)

@views.route('/search_results', methods=['GET', 'POST'])
def search_results():
    if request.method == 'POST':
        user_input_name = request.form['user_search']
        new_data = get_searched_tutors(user_input_name)
        return render_template("tutor_search.html", data=new_data)
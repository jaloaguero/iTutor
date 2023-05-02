#this file stores the routes for all static pages on website. 
#home, about us, etc.

from flask import Blueprint
from flask import render_template

views = Blueprint('views', __name__)

#defines route, in this case home = / cuz it goes nowhere. 
@views.route('/')
def home():
    return render_template("home.html")

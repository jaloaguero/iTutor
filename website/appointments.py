#for all pages that have to do w user authentication (login/signup)

#TODO: once u figure it out, clean up code, and move all code w sql to a different file
from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import g

from sql_scripts import get_email_tutors

appointments = Blueprint('appointments', __name__)

@appointments.route('/profile')
def profile():
    if g.user:
         new_data = get_email_tutors(g.user)
         print("NEW DATA: ")
         print(new_data)
         return render_template("profile.html", data=new_data)

    return redirect(url_for('auth.login'))


@appointments.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
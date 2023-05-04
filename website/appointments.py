#for all pages that have to do w user authentication (login/signup)

#TODO: once u figure it out, clean up code, and move all code w sql to a different file
from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import g

from sql_scripts import get_subjects

appointments = Blueprint('appointments', __name__)

@appointments.route('/appointments')
def protected():
    if g.user:
        return render_template('protected.html', user=session['user'])
        print(get_subjects)
    return redirect(url_for('auth.login'))
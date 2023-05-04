#for all pages that have to do w user authentication (login/signup)

#TODO: once u figure it out, clean up code, and move all code w sql to a different file
from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import g

appointments = Blueprint('appointments', __name__)

@appointments.route('/appointments')
def protected():
    print("got to protected somehow")
    if g.user:
        return render_template('protected.html', user=session['user'])
    return redirect(url_for('auth.login'))


@appointments.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']
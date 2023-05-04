#for all pages that have to do w user authentication (login/signup)

#TODO: once u figure it out, clean up code, and move all code w sql to a different file
from flask import Blueprint
from flask import render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
from flask import g

from sql_scripts import sql_signup_student, sql_signup_tutor, sql_login

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    #if request = post means its asking for information
    #so we drop it basically
    if request.method == 'POST':
        #session.pop() gets rid of user session and replaces it w none
        session.pop('user', None)
        #when login button pressed, login_submit becomes true
        login_submit = request.form.get("login_submit")
        #when signup button is pressed, signup_submit becomes true
        signup_submit = request.form.get("signup_submit")


        #login
        if login_submit is not None:
            input_email = request.form['email']
            input_password = request.form['password']

            are_credentials_valid = sql_login(input_email, input_password)

            if are_credentials_valid == True:
                session['user'] =request.form['email']
                return redirect(url_for('appointments.protected'))
            
        #signup
        if signup_submit is not None:
            print("Pressed Signup button")
            session.pop('user', None)

            #grabs information typed in from html file and saves it
            full_name = request.form['full_name']
            age = request.form['age']
            email = request.form['email']
            password = request.form['password']
            #grabs signup specific stuff
            password_confirm = request.form['password_confirm']
            student_or_tutor = request.form['account-type']
            #subjects = request.form['tutor-subject']

            age = int(age)

            #calls studentdatabase thing
            if student_or_tutor == 'student':

                subjects = request.form['subject']
                sql_signup_student(full_name, age, email, password, subjects)

            if student_or_tutor == 'tutor':
                description = request.form['description']
                profile_pic = request.form['avatar']
                subjects = request.form['tutor-subject']
                sql_signup_tutor(full_name, age, email, password, description, subjects, profile_pic)

            #TODO: create a webpage  that basically does this
            return "Information submitted to database succesfully"
    return render_template("login.html")


#TODO: this entire section is temporary, just checking stuff, will need a brand new
#route for both log in and sign up 
@auth.route('/protected')
def protected():
    if g.user:
        return render_template('protected.html', user=session['user'])
    return redirect(url_for('auth.login'))
    
#Holdover from previous stuff, pretty sure i don't need this but leaving it in case it breaks something
@auth.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@auth.route('/dropsession')
def dropsession():
    session.pop('user',None)
    return render_template('login.html')
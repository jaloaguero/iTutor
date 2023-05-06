from flask_mysqldb import MySQL
from database_init import db

from hash_passwords import hash_password, verify_password

mysql = db

#checks if user exists, and if password matches, returns bool
#MAY NEED TO BE MODIFIED TO HAVE STUDENT AND TUTOR
def sql_login(email, password):
    #declaring db_password up here and making it empty so it can be called later
    #declaring empty because an empty password CANNOT BE PASSED from above
    db_password = "notreal"
    #tells db to use the db, idk dude it doesnt work without this
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()

    #Looks for provided email, grabs password associated w it from db.
    #if it grabs nothing, db_password won't equal password anyways, so it will come back false
    #that way, we won't know if its the username or password that failed
    cur = mysql.connection.cursor()
    is_empty = cur.execute("SELECT password FROM itutordb.person WHERE email=%s;",[email] )
    #is_empty saves amount of things i got from cur.execute, i only asked for password so there should only be 1 thing

    if is_empty == 1:
        db_raw = cur.fetchall()
        db_password = db_raw[0][0]
    #grabs everything that i asked for in the execute, and saves it to db_raw
    mysql.connection.commit()
    cur.close()

    password = hash_password(password)

    if verify_password(db_password, password) == True:
        return True

    return False

#adds whatever info given to the database
#TODO: figure out how to give the damn thing pictures
#TODO: add function to add tutors and students, not just person
def sql_signup_student(name, age, email, password, subject):

    #hashes password
    password = hash_password(password)

    #tells db to use the db, idk dude i shouldn't need this but it doesnt work without this
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()


    #Creating a person, because both students and tutors are people
    cur = mysql.connection.cursor()
    #person_id (not needed cuz auto increment), name, age, email, passowrd, complete_hours
    cur.execute("INSERT INTO person values(NULL, %s, %s, %s, %s, 0);",(name, age, email, password))
    mysql.connection.commit()
    cur.close()

    print("Creating Student...")
    #Retrieves the person we have just created's pkey
    cur = mysql.connection.cursor()
    is_empty = cur.execute("SELECT person_id FROM person WHERE email = %s and password = %s;", (email,password))
    if is_empty == 1:
        db_raw = cur.fetchall()
        db_pkey = int(db_raw[0][0])
        #creates 
        cur.execute("INSERT INTO student values(%s, NULL, %s);",(db_pkey, subject))

    mysql.connection.commit()
    cur.close()

    return 0

def sql_signup_tutor(name, age, email, password, description, subject, profile_pic):

    #hashes password
    password = hash_password(password)

    #tells db to use the db, idk dude i shouldn't need this but it doesnt work without this
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()
    
    #Creating a person, because both students and tutors are people
    cur = mysql.connection.cursor()
    #person_id (not needed cuz auto increment), name, age, email, passowrd, complete_hours
    cur.execute("INSERT INTO person values(NULL, %s, %s, %s, %s, 0);",(name, age, email, password))
    mysql.connection.commit()
    cur.close()

    print("Creating Tutor...")
    #Retrieves the person we have just created's pkey
    cur = mysql.connection.cursor()
    is_empty = cur.execute("SELECT person_id FROM person WHERE email = %s and password = %s;", (email,password))
    if is_empty == 1:
        db_raw = cur.fetchall()
        db_pkey = int(db_raw[0][0])
        #creates 
        cur.execute("INSERT INTO tutor values(%s, %s, %s, %s);",(db_pkey, description, subject, profile_pic))

    mysql.connection.commit()
    cur.close()

    return 0

def is_email_used(email):
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    is_empty = cur.execute("SELECT password FROM itutordb.person WHERE email=%s;",[email] )
    #if is_empty == 1, means it actually got a result, so we return true
    if is_empty == 1:
        db_raw = cur.fetchall()
        print(db_raw)
        print("Just printed_db_raw")
        return True
    
    mysql.connection.commit()
    cur.close()

    return False

def get_all_tutors():
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    is_empty = cur.execute("SELECT * FROM tutor;")
    #if is_empty == 1, means it actually got a result, so we return false
    db_raw = cur.fetchall()
    
    mysql.connection.commit()
    cur.close()

    return db_raw

def get_name(pk):
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    is_empty = cur.execute("SELECT name FROM person where person_id=%s;",[pk])
    #if is_empty == 1, means it actually got a result, so we return false
    db_raw = cur.fetchall()
    
    mysql.connection.commit()
    cur.close()

    name = db_raw[0][0]

    return name

def get_age(pk):
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    is_empty = cur.execute("SELECT age FROM person where person_id=%s;",[pk])
    #if is_empty == 1, means it actually got a result, so we return false
    db_raw = cur.fetchall()
    
    mysql.connection.commit()
    cur.close()

    age = db_raw[0][0]

    return age

def get_email(pk):
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()

    cur = mysql.connection.cursor()
    is_empty = cur.execute("SELECT email FROM person where person_id=%s;",[pk])
    #if is_empty == 1, means it actually got a result, so we return false
    db_raw = cur.fetchall()
    
    mysql.connection.commit()
    cur.close()

    email = db_raw[0][0]

    return email

def get_all_tutor_info():
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()


    cur = mysql.connection.cursor()
    cur.execute("select * from person JOIN tutor ON person.person_id = tutor.FK_tutor_id ;")
    #if is_empty == 1, means it actually got a result, so we return false
    db_raw = cur.fetchall()
    
    mysql.connection.commit()
    cur.close()

    return db_raw


def get_searched_tutors(search):
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()

    search = '%'+search+'%'

    cur = mysql.connection.cursor()
    search = '%'+search+'%'
    cur.execute("select * from person JOIN tutor ON person.person_id = tutor.FK_tutor_id where name like %s;",[search])
    #if is_empty == 1, means it actually got a result, so we return false
    db_raw = cur.fetchall()

    print(db_raw)
    
    mysql.connection.commit()
    cur.close()

    return db_raw


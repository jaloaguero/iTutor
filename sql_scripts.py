from flask_mysqldb import MySQL

from database_init import db

mysql = db

#checks if user exists, and if password matches, returns bool
#MAY NEED TO BE MODIFIED TO HAVE STUDENT AND TUTOR
def sql_login(email, password):
    #declaring db_password up here and making it empty so it can be called later
    #declaring empty because an empty password CANNOT BE PASSED from above
    db_password = ""
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

    if db_password == password:
        return True

    return False

#adds whatever info given to the database
#TODO: figure out how to give the damn thing pictures
#TODO: add function to add tutors and students, not just person
def sql_signup(name, age, email, password, student_or_tutor):

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

    if student_or_tutor == 'student':
        #here we create a student.
        print("Creating Student...")
    else:
        print("Creating Tutor...")    

    return 0

#calls db, returns all info on subjects
def get_subjects():
    cur = mysql.connection.cursor()
    cur.execute("USE itutordb;")
    mysql.connection.commit()
    cur.close()

    #grabs everything from subjecct, returns it thats it
    cur = mysql.connection.cursor()
    is_empty = cur.execute("SELECT * FROM itutordb.subject")
    db_raw = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    print("DB RAW IS: " + str(db_raw))

    return db_raw
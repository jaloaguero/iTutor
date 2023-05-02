#Main.py basically runs the entire website
#IF CONFUSED, DOWNLOAD ALL FILES, RUN THIS FILE
from flask_mysqldb import MySQL
from website import create_app


from database_init import db


app = create_app()

#app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

#mysql config stuff here
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "223146"
app.config['MYQSL_DB'] = "itutordb"

#idk exactly waht this does so we are treading on shit territory
db.init_app(app)



#init web server.
if __name__ == '__main__':
    #debug=True means its in debug mode, turn this off once done
    app.run(debug=True)
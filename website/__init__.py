from flask import Flask
import os


#i could probably return an object to main.py to really clean up
#but im p sure the way it is now is fine only do if you have more time


def create_app():
    #__name__ = name of file ran
    app = Flask(__name__)


    app.config['SECRET_KEY'] = os.urandom(24)

    #importing to then register
    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    
    return app
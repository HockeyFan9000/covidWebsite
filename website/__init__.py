from flask import Flask, redirect, request, redirect, url_for, abort, send_from_directory, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import os
import imghdr
from werkzeug.utils import secure_filename


db = SQLAlchemy()
DB_NAME = "database.db"
image_name = "uploadedImage"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'a29d514860ba77c0bf87e1dbe6d13f22414559fc06a17c60f7e0c44b022b4785'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['UPLOAD_PATH'] = '/home/JoshuaShunk/covidWebsite/website/static/uploads/'
    #app.config['UPLOAD_PATH']  = 'website/static/uploads/'
    app.config['MAX_CONTENT_PATH'] = 1024 * 1024
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.jpeg', '.webp']

    db.init_app(app)

    from .views import views
    from .auth import auth
    from .create import create_blueprint
    from .imagePrediction import image_blueprint
    from .viewPast import past_blueprint

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(create_blueprint, url_prefix='/')
    app.register_blueprint(image_blueprint, url_prefix='/')
    app.register_blueprint(past_blueprint, url_prefix='/')

    from .models import User, Patient

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        #print('Created Database!')

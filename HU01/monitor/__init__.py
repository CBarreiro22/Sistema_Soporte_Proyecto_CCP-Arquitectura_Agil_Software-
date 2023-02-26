from datetime import datetime
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

# Define a Flask application factory function that creates a new Flask instance
# and configures it with database settings
def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app

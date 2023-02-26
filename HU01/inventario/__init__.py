from datetime import datetime
import queue
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

# Create an instance of Celery, a task queue system, for monitoring the health of the app's components
monitor = Celery(__name__, broker='redis://localhost:6379/2')

# Define a task for monitoring the health of the app's components
@monitor.task(name="monitor_heartbeat")
def enviar_estado_salud(cliente):
    pass

# Define a function to create the Flask app instance
def create_app(config_name):
    # Create the Flask app instance
    app = Flask(__name__)

    # Set the URI for the SQLite database that the app will use
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'

    # Disable tracking modifications to the SQLAlchemy object
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Enable propagating exceptions to the Flask app's error handlers
    app.config['PROPAGATE_EXCEPTIONS'] = True

    # Return the Flask app instance
    return app

# Define a function to monitor the health of the app's components in a background thread
def heartbeat():
    while True:
        # Define the arguments to the enviar_estado_salud task
        args = ('Estado de Salud Componente Inventario | ' + str(datetime.now()), )

        # Schedule the enviar_estado_salud task to run asynchronously
        enviar_estado_salud.apply_async(args)

        # Sleep for 10 seconds before repeating the loop
        time.sleep(10)

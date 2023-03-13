from threading import Thread
from producto import create_app, heartbeat
from .modelos import db
from .vistas import VistaTablaProductos
from flask_restful import Api

# Create a Flask application instance with a default configuration
app = create_app('default')

# Create an application context and push it to the context stack
app_context = app.app_context()
app_context.push()

# Initialize the database with the application instance
db.init_app(app)
db.create_all()

# Create a Flask-RESTful API instance and add a resource called "VistaTablaProductos"
api = Api(app)
api.add_resource(VistaTablaProductos, '/productos')

# Start a background thread to send heartbeat messages to the monitoring system
monitor = Thread(target=heartbeat)
monitor.start()

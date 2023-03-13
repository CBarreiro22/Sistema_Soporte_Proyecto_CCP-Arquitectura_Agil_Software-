from threading import Thread
from inventario import create_app, heartbeat
from .modelos import db
from .vistas import VistaTablaInventario
from flask_restful import Api

# Create a Flask app instance using the "default" configuration
app = create_app('default')

# Create an application context for the Flask app
app_context = app.app_context()

# Push the application context so it becomes the active context
app_context.push()

# Initialize the database with the Flask app
db.init_app(app)

# Create any missing database tables based on the models defined in the app
db.create_all()

# Create an instance of the Flask-RESTful API and add a resource to it
api = Api(app)
api.add_resource(VistaTablaInventario, '/inventario-productos')

# Start a background thread to monitor the health of the app's components
monitor = Thread(target=heartbeat)
monitor.start()

from gateway import create_app
from .vistas import Gateway
from flask_restful import Api

# Create a Flask application instance with a default configuration
app = create_app('default')

# Create an application context and push it to the context stack
app_context = app.app_context()
app_context.push()

# Create a Flask-RESTful API instance and add a resource called "VistaTablaProductos"
api = Api(app)
api.add_resource(Gateway, '/gateway/inventario/')
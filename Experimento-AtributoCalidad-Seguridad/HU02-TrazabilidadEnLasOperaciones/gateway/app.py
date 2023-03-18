from gateway import create_app
from .vistas import Gateway, VistaSecurity
from flask_restful import Api
from flask_jwt_extended import JWTManager

# Create a Flask application instance with a default configuration
app = create_app('default')

# Create an application context and push it to the context stack
app_context = app.app_context()
app_context.push()

# Create a Flask-RESTful API instance and add a resource called "Gateway"
api = Api(app)
urls = [
    '/gateway/orden-venta',
    '/gateway/orden-venta/<int:id_orden_venta>'
]
api.add_resource(Gateway, *urls)
api.add_resource(VistaSecurity, '/gateway/login')

jwt = JWTManager(app)
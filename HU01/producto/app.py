from threading import Thread
from producto import create_app, heartbeat
from .modelos import db
from .vistas import VistaTablaProductos
from flask_restful import Api

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaTablaProductos, '/productos')

monitor = Thread(target=heartbeat)
monitor.start()

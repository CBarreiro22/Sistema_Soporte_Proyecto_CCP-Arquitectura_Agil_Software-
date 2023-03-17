from ordenVenta import create_app
from .vistas import VistaOrdenesVentas,VistaOrdenVenta
from flask_restful import Api
from .modelos import db
from flask_jwt_extended import JWTManager

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaOrdenesVentas, '/ordenesventa')
api.add_resource(VistaOrdenVenta, '/ordenventa/<int:id_ordenVenta>')


# jwt = JWTManager(app)
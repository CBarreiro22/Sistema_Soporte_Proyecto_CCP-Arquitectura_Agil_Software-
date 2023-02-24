from ..modelos import db, Producto, ProductoSchema
from flask_restful import Resource

producto_schema = ProductoSchema()

class VistaTablaProductos(Resource):
    def get(self):
        return 'Comunicación API para listar productos'

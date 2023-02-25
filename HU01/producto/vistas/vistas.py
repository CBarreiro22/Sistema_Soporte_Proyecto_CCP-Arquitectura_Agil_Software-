from flask import request
from ..modelos import db, Producto, ProductoSchema
from flask_restful import Resource

producto_schema = ProductoSchema()


class VistaTablaProductos(Resource):
    def get(self):
        return 'Comunicación API para listar productos'

    def post(self):
        nuevo_producto = Producto(
            nombre=request.json["nombre"], precio=request.json["precio"])
        print("precio: ", request.json["precio"])
        db.session.add(nuevo_producto)
        db.session.commit()
        return producto_schema.dump(nuevo_producto)

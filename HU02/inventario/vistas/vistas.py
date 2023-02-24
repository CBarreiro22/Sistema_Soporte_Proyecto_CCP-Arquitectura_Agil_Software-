from flask_restful import Resource
from faker import Faker

from modelos import \
    db, ProductoSchema, Producto

producto_schema = ProductoSchema()


class VistaProducto(Resource):

    def get(self, id_orden):

        producto = Producto( \
            nombre= Faker().name(),
            existencia=Faker().random()
            )
        db.session.add(producto)
        db.session.commit()

        return {"resultado": producto_schema.dump(producto)}


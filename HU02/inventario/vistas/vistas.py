from flask_restful import Resource
from faker import Faker

from modelos import \
    db, ProductoSchema, Producto

producto_schema = ProductoSchema()


class VistaProducto(Resource):

    def get(self, id_orden):
        print("id_orden: ", id_orden)

        producto = Producto( \
            nombre=Faker().name(),
            existencia=1
        )
        db.session.add(producto)
        db.session.commit()
        print("producto_schema: ", producto_schema.dump(producto))
        return {"resultado": producto_schema.dump(producto)}

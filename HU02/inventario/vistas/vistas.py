import requests as requests
from flask import request, jsonify
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


class VistaMonitor(Resource):
    def get(self):
        """
        Endpoint que responde a una petición GET o POST y devuelve la misma información recibida.
        """
        #url = "https://b3059e7c-ac64-481a-aec0-e6821bbfe850.mock.pstmn.io/echo"

        # Realizar la solicitud get al otro servicio
        #respuesta = requests.get(url)

        # Obtener el resultado de la respuesta
        #resultado = respuesta.json()

        #data = request.args if request.method == 'GET' else request.json
        return "Success"

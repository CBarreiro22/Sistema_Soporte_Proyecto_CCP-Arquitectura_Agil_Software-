from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from datetime import datetime
import hashlib
from faker import Faker

from modelos import \
    db
    #Producto

# producto_schema = ProductoSchema()


class VistaProducto(Resource):
    def post(self, id_orden):

        # producto = Producto( \
        #     nombre=request.json["nombre"], \
        #     apellido=request.json["apellido"], \
        #     talla=float(request.json["talla"]), \
        #     peso=float(request.json["peso"]), \
        #     edad=float(request.json["edad"]), \
        #     ingreso=datetime.strptime(request.json["ingreso"], '%Y-%m-%d'), \
        #     brazo=float(request.json["brazo"]), \
        #     pecho=float(request.json["pecho"]), \
        #     cintura=float(request.json["cintura"]), \
        #     pierna=float(request.json["pierna"]), \
        #     entrenando=bool(request.json["entrenando"]), \
        #     razon=request.json["razon"], \
        #     terminado=datetime.strptime(request.json["terminado"], '%Y-%m-%d'), \
        #     usuario=usuario \
        #     )
        # usuario_schema.dump(usuario)
        # Devolver una respuesta con el resultado
        return {"resultado": "resultado"}


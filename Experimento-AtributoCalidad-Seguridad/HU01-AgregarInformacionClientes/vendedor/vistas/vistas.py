import random
import uuid

import requests as requests

from flask import request, jsonify
from flask_restful import Resource
from cryptography.fernet import Fernet

from modelos import \
    db, ProductoSchema, Cliente

FILE_KEY = 'resources/llave.key'

cliente_schema = ProductoSchema()

class utils ():
    def encriptar (data):
        with open(FILE_KEY, 'rb') as f:
            key = f.read()

        cipher = Fernet(key)
        return cipher.encrypt(data.encode('utf-8'))

    def desencriptar (data):
        with open(FILE_KEY, 'rb') as f:
            key = f.read()

        cipher = Fernet(key)
        data_desencriptada = cipher.decrypt (data)
        print(f"Mensaje descifrado: {data_desencriptada}")

class VistaCliente(Resource):

    def post(self,id_usuario):
        nombre_completo = utils.encriptar(request.json["nombre_completo"])
        email = utils.encriptar(request.json["email"])
        direccion = utils.encriptar(request.json["direccion"])
        numero_cuenta_banco = utils.encriptar(request.json["numero_cuenta_banco"])
        RFC = utils.encriptar(request.json["numero_cuenta_banco"])
        id_user = str(uuid.uuid4())
        cliente = Cliente (id = id_user, nombre_completo= nombre_completo, email=email, direccion= direccion, numero_cuenta_banco= numero_cuenta_banco, RFC= RFC)
        db.session.add(cliente)
        db.session.commit()
        consulta_cliente = Cliente.query.get_or_404(id_user)

        utils.desencriptar(consulta_cliente.nombre_completo)
        utils.desencriptar(consulta_cliente.email)
        utils.desencriptar(consulta_cliente.direccion)
        utils.desencriptar(consulta_cliente.RFC)
        return cliente_schema.dump(cliente),200





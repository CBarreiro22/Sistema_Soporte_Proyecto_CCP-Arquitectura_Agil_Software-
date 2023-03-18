from operator import concat
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource, abort
import requests
from requests import RequestException
from flask import request

servicios = {  # Configuración de servicios
    'ordenes-venta': 'http://127.0.0.1:5000/ordenesventa',
    'orden-venta': 'http://127.0.0.1:5000/ordenventa/'
}


class VistaSecurity(Resource):

    def post(self):
        identity = concat(request.json["usuario"], request.json["password"])
        token_de_acceso = create_access_token(identity=identity)
        return {"token": token_de_acceso}


class Gateway(Resource):

    @jwt_required()
    def post(self):
        response = requests.post(
            url=servicios['ordenes-venta'], json=request.json)
        return response.json()

    @jwt_required()
    def put(self, id_orden_venta):
        response = requests.put(
            url=servicios['orden-venta']+str(id_orden_venta), json=request.json)
        return response.json()

    @jwt_required()
    def delete(self, id_orden_venta):
        response = requests.delete(
            url=servicios['orden-venta']+str(id_orden_venta), json=request.json)
        return '', 204

from flask import request
from flask_jwt_extended import jwt_required, create_access_token
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from datetime import datetime
from .utilidad_reporte import UtilidadReporte
import hashlib
import requests


class VistaOrden(Resource):
    def post(self, id_orden):
        # Construir la URL de la solicitud post con la variable en el path
        url = f"http://localhost:8000/orden/productos/{id_orden}"

        # Realizar la solicitud post al otro servicio
        respuesta = requests.post(url)

        # Obtener el resultado de la respuesta
        resultado = respuesta.json()

        # if entrenador is None:
        #     return {"message:": "el entrenador no existe"}, 404

        # Devolver una respuesta con el resultado
        return {"resultado": resultado}

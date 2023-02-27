import random
from flask_restful import Resource
import requests

mi_lista_codigos_error = [500, 200]
status_code = 200


class VistaOrden(Resource):
    def post(self, id_orden):

        global status_code  # indicar que se está utilizando la variable global

        # generar un código de estado aleatorio
        status_code = random.choice(mi_lista_codigos_error)

        if status_code == 200:
            # Construir la URL de la solicitud post con la variable en el path
            url = f"http://127.0.0.1:8090/orden/productos/{id_orden}"

            # Realizar la solicitud get al otro servicio
            respuesta = requests.get(url)

            # Obtener el resultado de la respuesta
            resultado = respuesta.json()

            # Devolver una respuesta con el resultado
            return {"resultado": resultado}

        else:
            return {"status": "fail"}, status_code


class VistaMonitor(Resource):
    def get(self):
        global status_code

        if (status_code == 200):
            return "Success", status_code
        else:
            return "Fail", status_code
from flask_restful import Resource
import requests


class VistaOrden(Resource):
    def post(self, id_orden):
        # Construir la URL de la solicitud post con la variable en el path
        url = f"http://127.0.0.1:8080/orden/productos/{id_orden}"

        # Realizar la solicitud get al otro servicio
        respuesta = requests.get(url)

        # Obtener el resultado de la respuesta
        resultado = respuesta.json()

        # if entrenador is None:
        #     return {"message:": "el entrenador no existe"}, 404

        # Devolver una respuesta con el resultado
        return {"resultado": resultado}

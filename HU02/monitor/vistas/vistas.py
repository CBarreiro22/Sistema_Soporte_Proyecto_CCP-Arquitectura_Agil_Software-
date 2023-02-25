from datetime import time

from flask_restful import Resource
import requests
import time


class VistaMonitor(Resource):

    def monitorearInventario(self):
        """
        Monitorea la conexión a una dirección IP o host utilizando una API de ping.
        Muestra un mensaje si la conexión se pierde o se restablece.
        """
        estado_anterior = self.pingInventario()
        while True:
            estado_actual = self.pingInventario()
            if estado_actual != estado_anterior:
                if estado_actual:
                    print(f"La conexión a Inventario se ha restablecido.")
                else:
                    print(f"La conexión a Inventario se ha perdido.")
            estado_anterior = estado_actual
            time.sleep(5)

    @staticmethod
    def pingInventario():
        """
        Envía una solicitud GET a una API que realice un ping a una dirección IP o host específico.
        Devuelve True si la respuesta fue exitosa, False si no.
        """
        url = f"http://127.0.0.1:8080/ping"
        try:
            response = requests.get(url)
            if response.status_code == 200 and "Success" in response.text:
                print(response)
                return True
            else:
                return False
        except:
            return False


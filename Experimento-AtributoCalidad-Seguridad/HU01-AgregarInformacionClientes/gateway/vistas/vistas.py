from flask_restful import Resource, abort
import requests
from requests import RequestException

servicios = {  # Configuración de servicios
    'servicioInvetario': 'http://127.0.0.1:5000/inventario-productos',
}


class Gateway(Resource):
    def get(self):
        reintentosMaximo = 3
        reintentoActual = 0
        # 2 reintentos maximo
        while reintentoActual < reintentosMaximo:
            try:
                response = requests.get(
                    servicios['servicioInvetario'])  # Realizar solicitud al servicio1 y devolver respuesta
                response.raise_for_status()
                print(response)
                if (response.status_code == 200):
                    return response.json()
                else:
                    print(
                        f"Ocurrió un error en la solicitud HTTP al servicio Inventario")
                    reintentoActual = self.verificacionReintento(
                        reintentoActual, reintentosMaximo)
            except RequestException as e:
                print(f"Ocurrió un except en la solicitud HTTP al servicio Inventario")
                reintentoActual = self.verificacionReintento(
                    reintentoActual, reintentosMaximo)

    def verificacionReintento(self, reintentoActual, reintentosMaximo):
        reintentoActual = reintentoActual + 1
        if reintentoActual < reintentosMaximo:
            print(
                f"Reintento: #{reintentoActual} petición servicio OrdenVenta")
        else:
            print("Maximo reintentos hechos.")
            abort(500)
        return reintentoActual

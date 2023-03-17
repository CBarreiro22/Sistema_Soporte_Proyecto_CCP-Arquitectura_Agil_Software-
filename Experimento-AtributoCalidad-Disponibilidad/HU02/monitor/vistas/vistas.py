import datetime

from flask_restful import Resource
import requests
import time

from modelos import \
    db, LogMonitor


class VistaMonitor(Resource):

    def monitorear(self):

        """
        Monitorea la conexión a una dirección IP o host utilizando una API de ping.
        Muestra un mensaje si la conexión se pierde o se restablece.
        """

        estado_anterior_inventario = True

        estado_anterior_orden_venta = True
        while True:
            estado_actual_inventario = self.ping("http://127.0.0.1:8090/ping")

            self.inventario_ping(estado_actual_inventario, estado_anterior_inventario)
            estado_anterior_inventario = estado_actual_inventario

            estado_actual_orden_venta = self.ping("http://127.0.0.1:8070/ping")
            self.orden_venta_ping(estado_actual_orden_venta, estado_anterior_orden_venta)
            estado_anterior_orden_venta = estado_actual_orden_venta

            time.sleep(5)

    def orden_venta_ping(self, estado_actual_venta, estado_anterior_orden_venta):
        componente_orden_venta = "ordenVenta"
        if estado_actual_venta != estado_anterior_orden_venta:
            date_string_ordern_venta = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if estado_actual_venta:
                db.session.add(LogMonitor(horaFecha=date_string_ordern_venta, status="Conexion_Reestablecida",
                                          componente=componente_orden_venta))
                db.session.commit()
                print(date_string_ordern_venta, f" La conexión a ", componente_orden_venta, " se ha restablecido")
            else:
                db.session.add(LogMonitor(horaFecha=date_string_ordern_venta, status="Conexion_perdida",
                                          componente=componente_orden_venta))
                db.session.commit()
                print(date_string_ordern_venta, f" La conexión a ", componente_orden_venta, " se ha perdido ")

    def inventario_ping(self, estado_actual, estado_anterior_inventario):
        componente_inventario = "Inventario"
        if estado_actual != estado_anterior_inventario:
            date_string_inventario = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if estado_actual:
                db.session.add(LogMonitor(horaFecha=date_string_inventario, status="Conexion_Reestablecida",
                                          componente=componente_inventario))
                db.session.commit()
                print(date_string_inventario, f" La conexión a ", componente_inventario, " se ha restablecido.")
            else:
                db.session.add(LogMonitor(horaFecha=date_string_inventario, status="conexion_perdida",
                                          componente=componente_inventario))
                db.session.commit()
                print(date_string_inventario, f" La conexión a ", componente_inventario, " se ha perdido.")

    @staticmethod
    def ping(url):
        """
        Envía una solicitud GET a una API que realice un ping a una dirección IP o host específico.
        Devuelve True si la respuesta fue exitosa, False si no.
        """

        try:
            response = requests.get(url)
            if (response.status_code == 200 and "Success" in response.text):
                return True
            else:
                return False
        except:
            return False

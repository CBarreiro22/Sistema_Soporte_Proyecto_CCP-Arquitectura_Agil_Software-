import queue
from ..modelos import db, Inventario, InventarioSchema
from celery import Celery
from flask_restful import Resource

inventario_schema = InventarioSchema()


BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

celery = Celery(__name__, broker=BROKER_URL, backend=BACKEND_URL)


@celery.task(name="consultar_inventario_producto")
def consultar_inventario_producto():
    pass


monitor = Celery(__name__, broker='redis://localhost:6379/2')


@monitor.task(name="monitor_heartbeat")
def enviar_estado_salud(cliente):
    pass


class VistaTablaInventario(Resource):
    def get(self):
        args = ('********* Request Inventario *********',)
        enviar_estado_salud.apply_async(args)
        result = consultar_inventario_producto.apply_async(
            queue='inventario_producto')
        information = {}
        results = []
        inventario = result.get()
        # l = ['agua', 'manzanas']
        # item1 = 0
        # item = 0
        # count = 0
        # identificador = 0
        # for i in l:
        #     for j in inventario:
        #         if inventario[item1]['nombre'] == i:
        #             identificador = 1
        #             count = count + 1
        #             information['id'] = item
        #             information['precio'] = inventario[item1]['precio']
        #             information['existencias'] = count
        #             information['nombre'] = inventario[item1]['nombre']
        #         item1 = item1+1

        #     if identificador != 0:
        #         results.append(information)
        #     identificador = 0
        #     item1 = 0
        #     item = item+1
        # print(results)
        return inventario

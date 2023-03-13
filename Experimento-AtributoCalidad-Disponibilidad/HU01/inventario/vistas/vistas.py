import queue
from random import randint
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
        inventario = result.get()
        for i in inventario:
            i['existencia'] = str(randint(1, 100))
        return inventario

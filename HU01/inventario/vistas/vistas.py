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


class VistaTablaInventario(Resource):
    def get(self):
        result = consultar_inventario_producto.apply_async(
            queue='inventario_producto')
            #  id, nombre, precio
            # producto_id, existencia
            # --> id, nombre, precio, existencia
        return result.get()

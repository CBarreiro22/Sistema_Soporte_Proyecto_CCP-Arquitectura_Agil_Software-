import queue
from ..modelos import db, Inventario, InventarioSchema
from celery import Celery
from flask_restful import Resource

inventario_schema = InventarioSchema()
celery = Celery(__name__, broker='redis://localhost:6379/0')


@celery.task(name="consultar_inventario_producto")
def consultar_inventario_producto():
    pass


class VistaTablaInventario(Resource):
    def get(self):
        result = consultar_inventario_producto.apply_async(
            queue='inventario_producto')
        print(result.get())
        return result.get()

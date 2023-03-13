from ..app import db
from ..modelos import ProductoSchema, Producto
from datetime import datetime
from sqlite3 import Date
from celery import Celery
from celery.signals import task_postrun
from flask.globals import current_app

producto_schema = ProductoSchema()

BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

app = Celery(__name__, broker=BROKER_URL, backend=BACKEND_URL)


monitor = Celery(__name__, broker='redis://localhost:6379/2')


@monitor.task(name="monitor_heartbeat")
def enviar_estado_salud(cliente):
    pass


@app.task(name="consultar_inventario_producto")
def consultar_productos():
    # consultar de la base de datos la informaciòn de todos los productos y retornar el json: id, nombre, precio
    # return 'Respuesta cola de mensaje listado de productos - ' + str( datetime.now())
    args = ('********* Response Producto *********',)
    enviar_estado_salud.apply_async(args)
    return [producto_schema.dump(producto) for producto in Producto.query.all()]


@task_postrun.connect
def close_session(*args, **kwargs):
    pass

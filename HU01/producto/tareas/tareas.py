from datetime import datetime
from sqlite3 import Date
from celery import Celery
from celery.signals import task_postrun
from flask.globals import current_app


BROKER_URL = 'redis://localhost:6379/0'
BACKEND_URL = 'redis://localhost:6379/1'
CELERY_RESULT_BACKEND = 'db+sqlite:///results.sqlite'

app = Celery(__name__, broker=BROKER_URL, backend=BACKEND_URL)
#app = Celery(__name__, broker='redis://localhost:6379/0')


@app.task(name="consultar_inventario_producto")
def consultar_productos():
    #consultar de la base de datos la informaciòn de todos los productos y retornar el json: id, nombre, precio
    return 'Respuesta cola de mensaje listado de productos - ' + str( datetime.now())

@task_postrun.connect
def close_session(*args, **kwargs):
    pass

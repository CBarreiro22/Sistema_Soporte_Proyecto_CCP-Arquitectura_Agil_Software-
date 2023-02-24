from celery import Celery
from celery.signals import task_postrun
from flask.globals import current_app

app = Celery(__name__, broker='redis://localhost:6379/0')


@app.task(name="consultar_inventario_producto")
def consultar_productos():
    print('as')
    return 'Respuesta cola de mensaje listado de productos'

@task_postrun.connect
def close_session(*args, **kwargs):
    pass

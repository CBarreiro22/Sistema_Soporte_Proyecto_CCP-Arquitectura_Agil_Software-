from datetime import datetime
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from ..app import db
from ..modelos import Auditoria
from celery.signals import task_postrun
from flask.globals import current_app

queque = Celery('tasks', broker='redis://localhost:6379/0')


@queque.task(name="monitor_accion")
def enviar_accion(operacion, id_orden_venta, campo, valor_anterior, valor_nuevo, usuario):
    print('Fecha: '+str(datetime.now()) + '| Operacion: '+operacion + '| Id: ' +
          str(id_orden_venta)+'| Campo: ' + campo + '| Valor Anterior: ' + valor_anterior + '| Valor Nuevo: ' + valor_anterior+'| Usuario: '+usuario)
    nueva_auditoria = Auditoria(operacion=operacion, orden_venta_id=id_orden_venta, campo=campo,
                                valor_anterior=valor_anterior, valor_nuevo=valor_nuevo, usuario=usuario)
    db.session.add(nueva_auditoria)
    db.session.commit()


@task_postrun.connect
def close_session(*args, **kwargs):
    db.session.remove()

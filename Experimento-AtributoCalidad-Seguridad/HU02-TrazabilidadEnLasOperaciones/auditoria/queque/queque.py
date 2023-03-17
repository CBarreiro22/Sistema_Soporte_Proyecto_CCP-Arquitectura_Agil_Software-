from datetime import datetime
from celery import Celery

queque = Celery(__name__, broker='redis://localhost:6379')


@queque.task(name="monitor_accion")
def enviar_accion(operacion, id_orden_venta, campo, valor_anterior, valor_nuevo, usuario):
    print('Fecha: '+str(datetime.now())+ '| Operacion: '+operacion + '| Id: ' +
          str(id_orden_venta)+'| Campo: ' + campo + '| Valor Anterior: ' + valor_anterior + '| Valor Nuevo: ' + valor_nuevo+'| Usuario: '+usuario)

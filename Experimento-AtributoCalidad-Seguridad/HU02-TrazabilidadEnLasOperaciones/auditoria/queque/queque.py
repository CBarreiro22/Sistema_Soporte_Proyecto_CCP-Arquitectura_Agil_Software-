from celery import Celery

queque = Celery(__name__, broker='redis://localhost:6379')


@queque.task(name="monitor_accion")
def enviar_accion(cliente):
    print(cliente)

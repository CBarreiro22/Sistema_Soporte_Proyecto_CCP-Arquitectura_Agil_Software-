from celery import Celery

queque = Celery(__name__, broker='redis://localhost:6379/')


@queque.task(name="monitor_heartbeat")
def enviar_accion(cliente):
    print(cliente)

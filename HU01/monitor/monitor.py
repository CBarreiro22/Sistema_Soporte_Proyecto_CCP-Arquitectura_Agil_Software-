from datetime import datetime
from http import client
from sqlite3 import Date
from celery import Celery
from celery.signals import task_postrun
from flask.globals import current_app

monitor = Celery(__name__, broker='redis://localhost:6379/2')


@monitor.task(name="monitor_heartbeat")
def enviar_estado_salud(cliente):
    print(cliente)

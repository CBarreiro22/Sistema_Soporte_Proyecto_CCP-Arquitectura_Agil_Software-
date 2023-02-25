from datetime import datetime
import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery

monitor = Celery(__name__, broker='redis://localhost:6379/2')


@monitor.task(name="monitor_heartbeat")
def enviar_estado_salud(cliente):
    pass


def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['PROPAGATE_EXCEPTIONS'] = True
    return app


def heartbeat():
    while True:
        args = ('Estado de Salud Componente Producto | ' +
                str(datetime.now()), )
        enviar_estado_salud.apply_async(args)
        time.sleep(5)

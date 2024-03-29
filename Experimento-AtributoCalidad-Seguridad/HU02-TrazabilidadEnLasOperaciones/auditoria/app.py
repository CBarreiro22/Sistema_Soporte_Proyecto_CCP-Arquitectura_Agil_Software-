from auditoria import create_app
from flask_restful import Api
from .modelos import db
from celery import Celery

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

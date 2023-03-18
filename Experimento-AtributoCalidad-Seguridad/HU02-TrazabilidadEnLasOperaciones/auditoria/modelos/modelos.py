import datetime
from email.policy import default
import enum
from datetime import datetime
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import DateTime

db = SQLAlchemy()


class Auditoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operacion = db.Column(db.String(128))
    orden_venta_id = db.Column(db.String(128))
    campo = db.Column(db.String(128))
    valor_anterior = db.Column(db.String(128))
    valor_nuevo = db.Column(db.String(128))
    usuario = db.Column(db.String(128))
    fecha = db.Column(DateTime, default=datetime.now())

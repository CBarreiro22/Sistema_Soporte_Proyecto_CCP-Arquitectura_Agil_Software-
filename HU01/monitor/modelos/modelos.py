from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields, Schema

db = SQLAlchemy()

class Monitor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mensaje = db.Column(db.String(128))
    hora = db.Column(db.String(300))

class MonitorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Monitor
        load_instance = True
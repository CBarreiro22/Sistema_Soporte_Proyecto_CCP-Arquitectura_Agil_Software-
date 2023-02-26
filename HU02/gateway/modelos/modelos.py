from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class LogMonitor (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    horaFecha = db.Column(db.String(15))
    status = db.Column(db.String(15))
    componente =  db.Column(db.String(15))

class LogMonitorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = LogMonitor
        include_relationships = False
        include_fk = False
        load_instance = True

    id = fields.String()

import enum
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Estado(enum.Enum):
    CREADO = 1
    MODIFICADO = 2
    ELIMINADO = 3


class Auditoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idOrdenVenta = db.Column(db.Integer)
    estadoAccion = db.Column(db.Enum(Estado))
    fecha = db.Column(db.DateTime)


class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}


class AuditoriaSchema(SQLAlchemyAutoSchema):
    estado = EnumADiccionario(attribute=("estado"))

    class Meta:
        model = Auditoria
        include_relationships = True
        load_instance = True

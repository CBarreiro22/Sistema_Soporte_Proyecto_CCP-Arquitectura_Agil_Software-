import enum
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
import datetime
from sqlalchemy import DateTime

db = SQLAlchemy()


class Estado(enum.Enum):
    CREADO = 1
    ENVIADO = 2
    DESPACHADO = 3
    PAGADO = 4
    CANCELADO = 5


class OrdenVenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    direccionEnvio = db.Column(db.String(128))
    monto = db.Column(db.Numeric)
    usuario = db.Column(db.String(128))
    fecha = db.Column(DateTime, default=datetime.datetime.utcnow)
    estado = db.Column(db.Enum(Estado))


class EnumADiccionario(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return None
        return {"llave": value.name, "valor": value.value}


class OrdenVentaSchema(SQLAlchemyAutoSchema):
    estado = EnumADiccionario(attribute=("estado"))
    
    class Meta:
        model = OrdenVenta
        include_relationships = True
        load_instance = True
    
    monto = fields.String()

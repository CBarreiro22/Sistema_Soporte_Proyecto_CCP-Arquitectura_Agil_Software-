from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Cliente(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    nombre_completo = db.Column(db.String(255))
    email = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    numero_cuenta_banco =  db.Column(db.String(255))
    RFC = db.Column(db.String(255))


class ProductoSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Cliente
        include_relationships = False
        include_fk = False
        load_instance = True

    id = fields.String()
    existencia = fields.String()

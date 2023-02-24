from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Producto (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(128))
    existencia = db.Column(db.Numeric)
class ProductoSchema (SQLAlchemyAutoSchema):
    class Meta:
        model = Producto
        include_relationships = False
        include_fk = False
        load_instance = True

    id = fields.String()
    existencia = fields.String()
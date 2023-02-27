from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class Inventario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.String(128))
    existencia = db.Column(db.Numeric)


class InventarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Inventario
        load_instance = True

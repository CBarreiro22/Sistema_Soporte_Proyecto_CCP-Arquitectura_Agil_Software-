from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()


class OrdenVenta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    direccionEnvio = db.Column(db.String(128))
    fecha = db.Column(db.DateTime)
    estado = db.Column(db.String(128))


class OrdenSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = OrdenVenta
        load_instance = True

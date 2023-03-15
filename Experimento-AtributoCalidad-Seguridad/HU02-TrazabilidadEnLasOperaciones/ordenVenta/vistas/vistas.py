from flask import request
from ..modelos import db, OrdenVenta, OrdenVentaSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token

orden_venta_schema = OrdenVentaSchema()


class VistaOrdenesVentas(Resource):

    def post(self):
        nueva_orden = OrdenVenta(direccionEnvio=request.json["direccionEnvio"], fecha=request.json["fecha"],estado=request.json["estado"])
        db.session.add(nueva_orden)
        db.session.commit()
        return orden_venta_schema.dump(nueva_orden)

    def get(self):
        return [orden_venta_schema.dump(ca) for ca in OrdenVenta.query.all()]


class VistaOrdenVenta(Resource):

    def get(self, id_ordenVenta):
        return orden_venta_schema.dump(OrdenVenta.query.get_or_404(id_ordenVenta))

    def put(self, id_ordenVenta):
        ordenVenta = OrdenVenta.query.get_or_404(id_ordenVenta)
        ordenVenta.direccionEnvio = request.json.get("direccionEnvio", ordenVenta.direccionEnvio)
        ordenVenta.fecha = request.json.get("fecha", ordenVenta.fecha)
        ordenVenta.estado = request.json.get("estado", ordenVenta.estado)
        db.session.commit()
        return orden_venta_schema.dump(ordenVenta)

    def delete(self, id_ordenVenta):
        ordenVenta = OrdenVenta.query.get_or_404(id_ordenVenta)
        db.session.delete(ordenVenta)
        db.session.commit()
        return '', 204
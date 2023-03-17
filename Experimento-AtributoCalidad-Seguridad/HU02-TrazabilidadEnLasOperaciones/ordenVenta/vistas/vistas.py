from celery import Celery
from flask import request
from ..modelos import db, OrdenVenta, OrdenVentaSchema
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token

orden_venta_schema = OrdenVentaSchema()

queque = Celery(__name__, broker='redis://localhost:6379/2')


@queque.task(name="monitor_heartbeat")
def enviar_accion(cliente):
    pass


class VistaOrdenesVentas(Resource):

    def post(self):
        args = ('********* Nuevo Orden Venat *********',)
        enviar_accion.apply_async(args)
        nueva_orden = OrdenVenta(direccionEnvio=request.json["direccionEnvio"], fecha=request.json["fecha"],
                                 estado=request.json["estado"])
        db.session.add(nueva_orden)
        db.session.commit()
        return orden_venta_schema.dump(nueva_orden)

    def get(self):
        return [orden_venta_schema.dump(ca) for ca in OrdenVenta.query.all()]


class VistaOrdenVenta(Resource):

    def get(self, id_ordenVenta):
        return orden_venta_schema.dump(OrdenVenta.query.get_or_404(id_ordenVenta))

    def put(self, id_ordenVenta):
        args = ('********* Modificacion Orden Venta *********',)
        enviar_accion.apply_async(args)
        ordenVenta = OrdenVenta.query.get_or_404(id_ordenVenta)
        ordenVenta.direccionEnvio = request.json.get("direccionEnvio", ordenVenta.direccionEnvio)
        ordenVenta.fecha = request.json.get("fecha", ordenVenta.fecha)
        ordenVenta.estado = request.json.get("estado", ordenVenta.estado)
        db.session.commit()
        return orden_venta_schema.dump(ordenVenta)

    def delete(self, id_ordenVenta):
        args = ('********* Borrar Orden Venta *********',)
        enviar_accion.apply_async(args)
        ordenVenta = OrdenVenta.query.get_or_404(id_ordenVenta)
        db.session.delete(ordenVenta)
        db.session.commit()
        return '', 204

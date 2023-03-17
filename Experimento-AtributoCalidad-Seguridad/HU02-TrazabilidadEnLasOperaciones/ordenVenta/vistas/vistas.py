from celery import Celery
from flask import request
from sqlalchemy import Numeric
from ..modelos import db, OrdenVenta, OrdenVentaSchema
from flask_restful import Resource

orden_venta_schema = OrdenVentaSchema()

queque = Celery(__name__, broker='redis://localhost:6379')


@queque.task(name="monitor_accion")
def enviar_accion(operacion, id_orden_venta, campo, valor_anterior, valor_nuevo, usuario):
    pass


class VistaOrdenesVentas(Resource):

    def post(self):
        nueva_orden = OrdenVenta(
            direccionEnvio=request.json["direccionEnvio"], estado=request.json["estado"], monto=request.json["monto"], usuario=request.json["usuario"])
        db.session.add(nueva_orden)
        db.session.commit()
        enviar_accion.apply_async(
            ('CREATE', nueva_orden.id, '', '', '', nueva_orden.usuario))
        return orden_venta_schema.dump(nueva_orden)

    def get(self):
        return [orden_venta_schema.dump(ca) for ca in OrdenVenta.query.all()]


class VistaOrdenVenta(Resource):

    def get(self, id_orden_venta):
        return orden_venta_schema.dump(OrdenVenta.query.get_or_404(id_orden_venta))

    def put(self, id_orden_venta):
        orden_venta = OrdenVenta.query.get_or_404(id_orden_venta)
        direccion_envio = request.json.get("direccionEnvio")
        estado = request.json.get("estado")
        monto = request.json.get("monto")
        usuario = request.json.get("usuario")

        if orden_venta.direccionEnvio != direccion_envio:
            enviar_accion.apply_async(
                ('UPDATE', orden_venta.id, 'DIRECCION_ENVIO', orden_venta.direccionEnvio, direccion_envio, usuario))
        if orden_venta.estado.name != estado:
            enviar_accion.apply_async(
                ('UPDATE', orden_venta.id, 'ESTADO', orden_venta.estado.name, estado, usuario))
        if str(orden_venta.monto) != str(monto):
            enviar_accion.apply_async(
                ('UPDATE', orden_venta.id, 'MONTO', orden_venta.monto, monto, usuario))
        if orden_venta.usuario != usuario:
            enviar_accion.apply_async(
                ('UPDATE', orden_venta.id, 'USUARIO', orden_venta.usuario, usuario, usuario))

        orden_venta.direccionEnvio = direccion_envio or orden_venta.direccionEnvio
        orden_venta.estado = estado or orden_venta.estado
        orden_venta.monto = monto or orden_venta.monto
        orden_venta.usuario = usuario or orden_venta.usuario
        db.session.commit()
        return orden_venta_schema.dump(orden_venta)

    def delete(self, id_orden_venta):
        orden_venta = OrdenVenta.query.get_or_404(id_orden_venta)
        usuario = request.json.get("usuario")
        enviar_accion.apply_async(
            ('DELETE', orden_venta.id, '', '', '', usuario))
        db.session.delete(orden_venta)
        db.session.commit()
        return '', 204

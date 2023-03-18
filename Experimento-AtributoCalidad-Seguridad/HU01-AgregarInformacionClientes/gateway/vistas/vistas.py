from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource, abort
import requests
from requests import RequestException
from flask import request
from modelos import Usuario, db
import hashlib


servicios = {  # Configuración de servicios
    'servicioVendedor': 'http://127.0.0.1:8090/register/data/user/',
}

class VistaSignIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"]).first()
        if usuario is None:
            contrasena_encriptada = hashlib.md5(request.json["contrasena"].encode('utf-8')).hexdigest()
            nuevo_usuario = Usuario(usuario=request.json["usuario"], contrasena=contrasena_encriptada)
            db.session.add(nuevo_usuario)
            db.session.commit()
            # token_de_acceso = create_access_token(identity=nuevo_usuario.id)
            return {"mensaje": "usuario creado exitosamente", "id": nuevo_usuario.id}
        else:
            return {"mensaje": "El usuario ya existe"}, 404

class VistaLogIn(Resource):

    def post(self):
        contrasena_encriptada = hashlib.md5(request.json["contrasena"].encode('utf-8')).hexdigest()
        usuario = Usuario.query.filter(Usuario.usuario == request.json["usuario"],
                                       Usuario.contrasena == contrasena_encriptada).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso, "id": usuario.id}

class Gateway(Resource):

    @jwt_required()
    def post(self, id_usuario):
        data = request.json  # Obtener datos del cuerpo de la solicitud
        token = request.headers.get('Authorization').split(' ')[1]
        headers = {'Authorization': f'Bearer {token}'}
        response = requests.post(
            servicios['servicioVendedor'] + str(id_usuario), json=data, headers=headers)  # Agregar datos en el cuerpo de la solicitud
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ocurrió un error en la solicitud HTTP al servicio servicioVendedor")


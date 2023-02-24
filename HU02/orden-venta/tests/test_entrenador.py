import hashlib
import json
import unittest

from faker import Faker

from app import app
from modelos import db, Usuario, Entrenador


class testEntrenador(unittest.TestCase):

    def setUp(self):
        self.data_factory = Faker()
        self.entrenador = app.test_client()
        self.entrenadores_creados = []
        self.usuarios_creados = []


        self.nombre_usuario = 'test_' + self.data_factory.name()
        contrasena = 'T1$' + self.data_factory.word()
        contrasena_encriptada = hashlib.md5(contrasena.encode('utf-8')).hexdigest()

        # Se crea el usuario para identificarse en la aplicación
        usuario_nuevo = Usuario(usuario=self.nombre_usuario, contrasena=contrasena_encriptada)
        db.session.add(usuario_nuevo)
        db.session.commit()


        usuario = Usuario.query.filter(Usuario.usuario == self.nombre_usuario).first()
        self.usuarios_creados.append(usuario)

        usuario_login = {
            "usuario": self.nombre_usuario,
            "contrasena": contrasena
        }

        solicitud_login = self.entrenador.post("/login",
                                           data=json.dumps(usuario_login),
                                           headers={'Content-Type': 'application/json'})

        respuesta_login = json.loads(solicitud_login.get_data())
        self.token = respuesta_login["token"]


    def test_crear_entrenador(self):
        nombre_usuario = 'test_' + self.data_factory.name()
        contrasena = 'T1$' + self.data_factory.word()
        nombre_entrenador = 'test_' + self.data_factory.name()
        apllidos_entrenador = 'test_' + self.data_factory.name()
        usuario_entrenador = {
            "usuario": nombre_usuario,
            "contrasena": contrasena,
            "nombre": nombre_entrenador,
            "apellido": apllidos_entrenador
        }

        entrenador_signup = self.entrenador.post("/signin",
                                                 data=json.dumps(usuario_entrenador),
                                                 headers={'Content-Type': 'application/json', 'status_code': 200})

        respuesta_signup = json.loads(entrenador_signup.get_data())

        usuario_id = respuesta_signup["id"]

        usuario_entrenador = Usuario.query.filter(Usuario.usuario == nombre_usuario).first()

        self.usuarios_creados.append(usuario_entrenador)
        self.assertEqual(entrenador_signup.status_code, 200)
        self.assertIsNotNone(respuesta_signup['id'])
        self.assertEqual(respuesta_signup['mensaje'], "usuario creado exitosamente")

    def test_crear_entrenador_existente(self):
        nombre_usuario = self.nombre_usuario
        contrasena = 'T1$' + self.data_factory.word()
        nombre_entrenador = 'test_' + self.data_factory.name()
        apllidos_entrenador = 'test_' + self.data_factory.name()
        usuario_entrenador = {
            "usuario": nombre_usuario,
            "contrasena": contrasena,
            "nombre": nombre_entrenador,
            "apellidos": apllidos_entrenador
        }

        entrenador_signup = self.entrenador.post("/signin",
                                                 data=json.dumps(usuario_entrenador),
                                                 headers={'Content-Type': 'application/json'})

        respuesta_signup = json.loads(entrenador_signup.get_data())
        self.assertEqual(entrenador_signup.status_code, 404)
        self.assertEqual(respuesta_signup['mensaje'], "El usuario ya existe")

    def tearDown(self):
        for usuario_creado in self.usuarios_creados:
            usuario = Usuario.query.filter(Usuario.id == usuario_creado.id).first()
            db.session.delete(usuario)

        db.session.commit()

        for entrenador_creado in self.entrenadores_creados:
            entrenador_id = Entrenador.query.get(entrenador_creado.id)
            db.session.delete(entrenador_id)
            db.session.commit()

    def test_listar_entrenadores(self):
        # Generar 10 entrenadores con datos aleatorios
        self.entrenadores_creados = []
        for i in range(0, 10):
            # Crear los datos del entrenador
            nombre_entrenador = self.data_factory.sentence()
            apellido_entrenador = self.data_factory.sentence()

            # Crear el entrenador con los datos originales para obtener su id
            entrenador = Entrenador(nombre=nombre_entrenador,
                                    apellidos=apellido_entrenador,
                                    usuario=1)
            db.session.add(entrenador)
            db.session.commit()
            self.entrenadores_creados.append(entrenador)

        # Definir endpoint, encabezados y hacer el llamado
        endpoint_entrenadores = "/entrenadores"
        headers = {'Content-Type': 'application/json', "Authorization": "Bearer {}".format(self.token)}

        resultado_consulta_entrenadores = self.entrenador.get(endpoint_entrenadores,
                                                          headers=headers)

        # Obtener los datos de respuesta y dejarlos un objeto json
        datos_respuesta = json.loads(resultado_consulta_entrenadores.get_data())

        # Verificar que el llamado fue exitoso
        self.assertEqual(resultado_consulta_entrenadores.status_code, 200)

        # Verificar los entrenadores creados con sus datos
        for entrenador in datos_respuesta:
            for entrenador_creado in self.entrenadores_creados:
                if entrenador['id'] == str(entrenador_creado.id):
                    self.assertEqual(entrenador['nombre'], entrenador_creado.nombre)
                    self.assertEqual(entrenador['apellidos'], entrenador_creado.apellidos)
                    self.assertEqual(entrenador['usuario'], str(entrenador_creado.usuario))

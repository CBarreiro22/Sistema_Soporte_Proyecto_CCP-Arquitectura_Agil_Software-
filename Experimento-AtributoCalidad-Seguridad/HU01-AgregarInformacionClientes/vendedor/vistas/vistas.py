import random
from flask_restful import Resource
from faker import Faker

from modelos import \
    db, ProductoSchema, Producto

producto_schema = ProductoSchema()
mi_lista_codigos_error = [500, 200]
status_code = 200

class VistaProducto(Resource):

    def get(self, id_orden):
        print("id_orden: ", id_orden)
        
        global status_code  # indicar que se está utilizando la variable global
        
        # generar un código de estado aleatorio
        status_code = random.choice(mi_lista_codigos_error)
        
        if status_code == 200:
            producto = Producto( \
                nombre=Faker().name(),
                existencia=1
            )
            db.session.add(producto)
            db.session.commit()
            print("producto_schema: ", producto_schema.dump(producto))
            
            return {"resultado": producto_schema.dump(producto)},200
        else:
            return {"status": "fail"},status_code


class VistaMonitor(Resource):
    def get(self):
        
        global status_code   
        
        if (status_code == 200):
            return "Success",status_code
        else:
            return "Fail",status_code
        

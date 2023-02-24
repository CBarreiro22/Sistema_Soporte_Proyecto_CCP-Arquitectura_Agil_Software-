from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from modelos import db
from vistas import \
    VistaProducto, VistaMonitor

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dbapp.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaProducto, '/orden/productos/<int:id_orden>')
api.add_resource(VistaMonitor, '/ping')

if __name__ == "__main__":
    app.run(debug=True, port=8080)

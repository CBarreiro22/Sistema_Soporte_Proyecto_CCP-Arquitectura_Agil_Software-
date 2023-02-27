from datetime import datetime
from http import client
from sqlite3 import Date
from celery import Celery
from celery.signals import task_postrun
from flask.globals import current_app
from flask_sqlalchemy import SQLAlchemy
#from .modelos import MonitorSchema,db

from .modelos import Monitor



#monitor_schema = MonitorSchema()


# Import the Celery library and set up a broker connection
monitor = Celery(__name__, broker='redis://localhost:6379/2')

# Initialize global variables for identifying and counting heartbeats
identificator = 0
count = 0
contStatehealthComponentI=0
ProductoComponentHealth=0

# Define a task called "enviar_estado_salud" to send health status updates
# to the monitoring system
@monitor.task(name="monitor_heartbeat")
def enviar_estado_salud(cliente):
    global identificator
    global count
    global contStatehealthComponentI
    global ProductoComponentHealth
    Component = cliente[27]+cliente[28]+cliente[29]+cliente[30]+cliente[31]+cliente[32]

    # Increment the state health counter for the relevant component
    ProductoComponentHealth = ProductoComponentHealth + 1

     # Increment the state health counter for the relevant component
    contStatehealthComponentI += 1

    # Check if the heartbeat message is a Request Inventario message
    if(cliente == '********* Request Inventario *********'):
        identificator = identificator + 1

    # Check if the heartbeat message is a Response Producto message
    if(cliente == '********* Response Producto *********'):
        identificator = identificator + 1
        count = 0

    # If the identificator is 1, increment the count
    if(identificator == 1):
        count = count + 1

    # If the identificator is 2, reset it to 0
    elif(identificator == 2):
        identificator = 0

    # If the count exceeds 3, log a message to a file indicating a
    # connection failure between the inventario and producto systems
    if(count > 3):
        with open('log.txt', 'a+') as file:
            file.write('[' + str(datetime.now()) + ']' + '- Falla en la cola de conexion entre inventario/producto\n')
        nuevoMonitor = Monitor(mensaje='Falla en la cola de conexion entre inventario/producto',hora=str(datetime.now()))
        """ db.session.add(nuevoMonitor)
        db.session.commit() """

    # Check if the component is "Inventario" and reset the state health counter if it is
    if Component == 'Invent':
        contStatehealthComponentI = 0


    # If the state health counter for the "Inventario" component exceeds a threshold,
    # write a log message indicating a failure in the inventory component
    if contStatehealthComponentI > 6:
        with open('logComponenteInventario.txt', 'a+') as file:
            file.write('[' + str(datetime.now()) + ']' + '- Falla Componente Inventario\n')
        nuevoMonitor = Monitor(mensaje='Falla Componente Inventario',hora=str(datetime.now()))
        """ db.session.add(nuevoMonitor)
        db.session.commit() """
        
        


    # Check if the component is "Producto" and reset the state health counter if it is
    if Component == 'Produc':
        ProductoComponentHealth = 0


    # If the state health counter for the "Producto" component exceeds a threshold ,
    # write a log message indicating a failure in the product component
    if ProductoComponentHealth> 6:
        with open('logComponenteProducto.txt', 'a+') as file:
            file.write('[' + str(datetime.now()) + ']' + '- Falla Componente Producto\n')
        nuevoMonitor = Monitor(mensaje='Falla Componente Producto',hora=str(datetime.now()))
        """ db.session.add(nuevoMonitor)
        db.session.commit() """
        print('Ingreso')
    
    
    
    # Print a message indicating the client that sent the heartbeat
    print(cliente)
    

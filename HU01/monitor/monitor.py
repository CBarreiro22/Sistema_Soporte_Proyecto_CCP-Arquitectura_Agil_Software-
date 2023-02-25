from datetime import datetime
from http import client
from sqlite3 import Date
from celery import Celery
from celery.signals import task_postrun
from flask.globals import current_app

# Import the Celery library and set up a broker connection
monitor = Celery(__name__, broker='redis://localhost:6379/2')

# Initialize global variables for identifying and counting heartbeats
identificator = 0
count = 0

# Define a task called "enviar_estado_salud" to send health status updates
# to the monitoring system
@monitor.task(name="monitor_heartbeat")
def enviar_estado_salud(cliente):
    global identificator
    global count

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

    # Print a message indicating the client that sent the heartbeat
    print('Hola Esto es cliente: ', cliente)

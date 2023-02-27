# Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-

Clonar repositorio:
> git clone https://github.com/CBarreiro22/Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-

## Detección de falla de los microservicios Invetario y Producto mediante componente Monitor

### Táctica: Heartbeat 
### Pasos para probar el experimento:
* Abrir una terminal de windows/terminal de comandos, ubicarse dentro de la carpeta HU01 del proyecto recién clonado y crear el ambiente virtual de python mediante la siguiente instrucción ``` python3 -m venv env```
* Una vez creado el ambiente, proceder con la activación del ambiente mediante el comando ```source venv/bin/activate```
* Instalar las dependencias para este proyecto mediante el siguiente comando ```pip install -r requeriments.txt```
* Abrir una nueva terminal de comandos e iniciar el servidor redis mediante el comando ```redis-server```
* Abrir una nueva terminal de comandos y desplegar la cola de mensajes Monitor, ingresamos al directorio HU01 y ejecutamos el siguiente comando ```celery -A monitor worker -l info``
* Abrir una nueva terminal de comandos y desplegar el microservicio Inventario, ingresando dentro del directorio HU01/inventario y ejecutar el comando ```flask run -p 5000```
* Abrir una nueva terminal de comandos y desplegar el microservicio Producto, ingresando dentro del directorio HU01/producto y ejecutar el comando ```flask run -p 5001```
* Detener el microservicio Producto. Ir a la terminal donde se ejecutó el comando para microserivcio Producto y presionar las teclas ```Ctrl C``` para detener el servicio.
* Esperar unos momentos (1 minuto aproximandamente) y revisar que en el archivo de log, HU01/logComponenteProducto.txt se haya registrado una entrada de falla de componente.

## Resultados
* Se puede consultar los archivos logs HU01/logComponenteProducto.txt y HU01/logComponenteInvetario.txt

### Notas
* De manera similar se puede validar la falla del componente Inventario, para el cual es necesario detener el microservicio Invetario (siguiendo los pasos previamente indicados para microservicio Producto) y revisar el log en el archivo HU01/logComponenteInventario.txt
* Si desea activar el microservicio Producto lo puede realizar siguiendo los pasos que se indicaron previamente para inicio de microservicio (```flask run -p 5001```)

## Detección de falla de la cola de mensajes invetario-producto mediante componente Monitor

### Táctica: Heartbeat 
### Pasos para probar el experimento:
* Abrir una terminal de windows/terminal de comandos, ubicarse dentro de la carpeta HU01 del proyecto recién clonado y crear el ambiente virtual de python mediante la siguiente instrucción ``` python3 -m venv env```
* Una vez creado el ambiente, proceder con la activación del ambiente mediante el comando ```source venv/bin/activate```
* Instalar las dependencias para este proyecto mediante el siguiente comando ```pip install -r requeriments.txt```
* Abrir una nueva terminal de comandos e iniciar el servidor redis mediante el comando ```redis-server```
* Abrir una nueva terminal de comandos y desplegar la cola de mensajes monitor, ingresamos al directorio HU01 y ejecutamos el siguiente comando ```celery -A monitor worker -l info``
* Abrir una nueva terminal de comandos y desplegar la cola de mensajes inventario-producto, ingresar dentro del directorio HU01 y ejecutar el siguiente comando ```celery -A producto.tareas worker  -l info -Q inventario_producto```
* En la misma ventana terminal de comandos, desplegar el microservicio Inventario, ingresando dentro del directorio HU01/inventario y ejecutar el comando ```flask run -p 5000```
* Abrir una nueva terminal de comandos y desplegar el microservicio Producto, ingresando dentro del directorio HU01/producto y ejecutar el comando ```flask run -p 5001```
* Abrir una nueva terminal de comandos y desplegar el gateway , ingresando dentro del directorio HU01/gateway y ejecutar el comando ```flask run -p 5002```
* Abrir postman y realizar una petición ```get``` a la siguiente dirección ```http://127.0.0.1:5002/gateway/inventario/```
* Los resultados de consulta de productos se mostrarán en la respuesta de la petición postman
* Ir a la terminal donde fue desplegado la cola de mensajes invetario-producto y presionar las teclas ```Ctrl C``` para detener la cola.
* Abrir postman y realizar una petición ```get``` a la siguiente dirección ```http://127.0.0.1:5002/gateway/inventario/```
* Esperar unos momentos (1 minuto aproximandamente) y revisar que en el archivo de log, HU01/log.txt se haya registrado una entrada de falla de la cola de mensaje inventario-producto.

## Resultados
* Se puede consultar los archivos logs HU01/logComponenteProducto.txt y HU01/logComponenteInvetario.txt

### Notas
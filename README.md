# Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-

## Clonar repositorio:
> git clone https://github.com/CBarreiro22/Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-

## Experimento Atributo de Calidad Disponibilidad

<details>
<summary>HU01 - Visualizacion de Productos</summary>

### Enlace
[Enlace](https://github.com/CBarreiro22/Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-/issues/1)

### Video
[Enlace](https://uniandes-my.sharepoint.com/personal/c_barreiroh_uniandes_edu_co/_layouts/15/stream.aspx?id=%2Fpersonal%2Fc%5Fbarreiroh%5Funiandes%5Fedu%5Fco%2FDocuments%2Fvideo1581746771%2Emp4&ga=1)

### Detección de falla de los microservicios Inventario y Producto mediante componente Monitor

#### Táctica: Heartbeat 

#### Pasos para probar el experimento:
* Abrir una terminal de windows/terminal de comandos, ubicarse dentro de la carpeta HU01 del proyecto recién clonado y crear el ambiente virtual de python mediante la siguiente instrucción ``` python3 -m venv env```
* Una vez creado el ambiente, proceder con la activación del ambiente mediante el comando ```source venv/bin/activate```
* Instalar las dependencias para este proyecto mediante el siguiente comando ```pip install -r requeriments.txt```
* Abrir una nueva terminal de comandos e iniciar el servidor redis mediante el comando ```redis-server```
* Abrir una nueva terminal de comandos y desplegar la cola de mensajes Monitor, ingresamos al directorio HU01 y ejecutamos el siguiente comando ```celery -A monitor worker -l info```
* Abrir una nueva terminal de comandos y desplegar el microservicio Inventario, ingresando dentro del directorio HU01/inventario y ejecutar el comando ```flask run -p 5000```
* Abrir una nueva terminal de comandos y desplegar el microservicio Producto, ingresando dentro del directorio HU01/producto y ejecutar el comando ```flask run -p 5001```
* Detener el microservicio Producto. Ir a la terminal donde se ejecutó el comando para microserivcio Producto y presionar las teclas ```Ctrl + C``` para detener el servicio.
* Esperar unos momentos (1 minuto aproximandamente) y revisar que en el archivo de log, ```HU01/logComponenteProducto.txt``` se haya registrado una entrada de falla de componente.

#### Resultados
* Se puede consultar los archivos logs ```HU01/logComponenteProducto.txt``` y ```HU01/logComponenteInventario.txt```

<img width="1010" alt="image" src="https://user-images.githubusercontent.com/94886747/221461249-685dbe06-76e9-4c48-ae15-8cb7a642d7f3.png">
<img width="999" alt="image" src="https://user-images.githubusercontent.com/94886747/221454486-779054c8-34db-424e-bd74-712f3167c361.png">
<img width="999" alt="image" src="https://user-images.githubusercontent.com/94886747/221454618-bac4f679-7452-433b-bee4-c9a796a768d5.png">


#### Notas
* De manera similar se puede validar la falla del componente Inventario, para el cual es necesario detener el microservicio Invetario (siguiendo los pasos previamente indicados para microservicio Producto) y revisar el log en el archivo ```HU01/logComponenteInventario.txt```
* Si desea activar el microservicio Producto lo puede realizar siguiendo los pasos que se indicaron previamente para inicio de microservicio (```flask run -p 5001```)

### Detección de falla de la cola de mensajes invetario-producto mediante componente Monitor

#### Táctica: Heartbeat 

#### Pasos para probar el experimento:
* Abrir una terminal de windows/terminal de comandos, ubicarse dentro de la carpeta HU01 del proyecto recién clonado y crear el ambiente virtual de python mediante la siguiente instrucción ``` python3 -m venv env```
* Una vez creado el ambiente, proceder con la activación del ambiente mediante el comando ```source venv/bin/activate```
* Instalar las dependencias para este proyecto mediante el siguiente comando ```pip install -r requeriments.txt```
* Abrir una nueva terminal de comandos e iniciar el servidor redis mediante el comando ```redis-server```
* Abrir una nueva terminal de comandos y desplegar la cola de mensajes monitor, ingresamos al directorio HU01 y ejecutamos el siguiente comando ```celery -A monitor worker -l info```
* Abrir una nueva terminal de comandos y desplegar la cola de mensajes inventario-producto, ingresar dentro del directorio HU01 y ejecutar el siguiente comando ```celery -A producto.tareas worker  -l info -Q inventario_producto```
* En la misma ventana terminal de comandos, desplegar el microservicio Inventario, ingresando dentro del directorio HU01/inventario y ejecutar el comando ```flask run -p 5000```
* Abrir una nueva terminal de comandos y desplegar el microservicio Producto, ingresando dentro del directorio HU01/producto y ejecutar el comando ```flask run -p 5001```
* Abrir una nueva terminal de comandos y desplegar el gateway , ingresando dentro del directorio HU01/gateway y ejecutar el comando ```flask run -p 5002```
* Abrir postman y realizar una petición ```get``` a la siguiente dirección ```http://127.0.0.1:5002/gateway/inventario/```
* Los resultados de consulta de productos se mostrarán en la respuesta de la petición postman
* Ir a la terminal donde fue desplegado la cola de mensajes invetario-producto y presionar las teclas ```Ctrl + C``` para detener la cola.
* Abrir postman y realizar una petición ```get``` a la siguiente dirección ```http://127.0.0.1:5002/gateway/inventario/```
* Esperar unos momentos (1 minuto aproximandamente) y revisar que en el archivo de log, ```HU01/log.txt``` se haya registrado una entrada de falla de la cola de mensaje inventario-producto.

#### Resultados
* Se puede consultar el archivo de logs ```HU01/log.txt```

<img width="1010" alt="image" src="https://user-images.githubusercontent.com/94886747/221461446-b1ea7a86-295b-4fa2-bad2-e43120f49ca7.png">
<img width="1010" alt="image" src="https://user-images.githubusercontent.com/94886747/221461645-e5084537-b7ed-49d8-980e-19c44e295a54.png">
<img width="1619" alt="image" src="https://user-images.githubusercontent.com/94886747/221454847-8d4cda11-f7c2-4bac-a7ce-5b8a1ffa4577.png">
<img width="999" alt="image" src="https://user-images.githubusercontent.com/94886747/221454645-925f3758-b35a-40be-811d-49b844872875.png">

#### Notas
</details>

<details>
<summary>HU02 - Recepcion de pedidos</summary>

### Enlace
[Enlace](https://github.com/CBarreiro22/Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-/issues/2)

### Video
[Enlace](https://uniandes-my.sharepoint.com/personal/i_oliva_uniandes_edu_co/_layouts/15/stream.aspx?id=%2Fpersonal%2Fi%5Foliva%5Funiandes%5Fedu%5Fco%2FDocuments%2FArquitecturas%20agiles%2FSemana%205%2FDemo%20experimento%2Emp4&ga=1)

#### Pasos para probar el experimento:
1. Configurar el venv 

2. Ir a la carpeta HU02 y abrir cada carpeta en una consola separada. 

3. Ejecutar proyecto en cada directorio.



    mac
    ```console
    python3 app.py
    ```
    windows
    ```console
    python app.py
    ```
    Una vez iniciados Inventario, Orden Venta, monitor y API Gateway

4. Correr el llamado API de postman
[Postman Collection](https://documenter.getpostman.com/view/23921893/2s93CPrYR2)
</details>

## Experimento Atributo de Calidad Seguridad

<details>
<summary>HU01 - Agregar Información Clientes</summary>
</details>

<details>
<summary>HU02 - Trazabilidad En Las Operaciones</summary>

### Enlace
[Enlace](https://github.com/CBarreiro22/Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-/issues/21)

### Video
[Video]()

### Descripción de experimento para Integridad

#### Tácticas: Recuperarse de ataques (Manejo de logs de eventos y Autenticación)

#### Pasos para probar el experimento:
* Abrir una terminal de windows/terminal de comandos, ubicarse dentro de la carpeta HU01 del proyecto recién clonado y crear el ambiente virtual de python mediante la siguiente instrucción ``` python3 -m venv env```
* Una vez creado el ambiente, proceder con la activación del ambiente mediante el comando ```source venv/bin/activate```
* Instalar las dependencias para este proyecto mediante el siguiente comando ```pip install -r requirements.txt```
* Abrir una nueva terminal de comandos e iniciar el servidor redis mediante el comando ```redis-server```
* Abrir una nueva terminal de comandos y desplegar la cola de mensajes monitor, ingresamos al directorio ```Experimento-AtributoCalidad-Seguridad/HU02-TrazabilidadEnLasOperaciones``` y ejecutamos el siguiente comando ```celery -A auditoria.queque worker -l info```
* Abrir una nueva terminal de comandos y desplegar la cola de mensajes inventario-producto, ingresar dentro del directorio ```Experimento-AtributoCalidad-Seguridad/HU02-TrazabilidadEnLasOperaciones/ordenVenta``` y ejecutar el siguiente comando ```flask run```
* Abrir una nueva terminal de comandos y desplegar el gateway , ingresando dentro del directorio ```Experimento-AtributoCalidad-Seguridad/HU02-TrazabilidadEnLasOperaciones/gateway``` y ejecutar el comando ```flask run -p 5001```
* Abrir postman y realizar una petición ```get``` a la siguiente dirección ```http://127.0.0.1:5001/gateway/inventario/```
* Los resultados de consulta de productos se mostrarán en la respuesta de la petición postman
* Ir a la terminal donde fue desplegado la cola de mensajes invetario-producto y presionar las teclas ```Ctrl + C``` para detener la cola.
* Abrir postman y realizar una petición ```get``` a la siguiente dirección ```http://127.0.0.1:5001/gateway/inventario/```
* Esperar unos momentos (1 minuto aproximandamente) y revisar que en el archivo de log, ```HU01/log.txt``` se haya registrado una entrada de falla de la cola de mensaje inventario-producto.

#### Resultados

#### Notas

</details>






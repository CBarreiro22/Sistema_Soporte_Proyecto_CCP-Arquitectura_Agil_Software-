# Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-

## Clonar repositorio:
> git clone https://github.com/CBarreiro22/Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-

## Experimento 1 Atributo de Calidad Disponibilidad

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

## Experimento 2 Atributo de Calidad Seguridad

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
* Abrir una nueva terminal de comandos y desplegar la cola de mensajes Auditoria, ingresamos al directorio ```Experimento-AtributoCalidad-Seguridad/HU02-TrazabilidadEnLasOperaciones``` y ejecutamos el siguiente comando ```celery -A auditoria.queque worker -l info```
* Abrir una nueva terminal de comandos y desplegar el microservicio ordenVenta, ingresar dentro del directorio ```Experimento-AtributoCalidad-Seguridad/HU02-TrazabilidadEnLasOperaciones/ordenVenta``` y ejecutar el siguiente comando ```flask run```
* Abrir una nueva terminal de comandos y desplegar el gateway , ingresando dentro del directorio ```Experimento-AtributoCalidad-Seguridad/HU02-TrazabilidadEnLasOperaciones/gateway``` y ejecutar el comando ```flask run -p 5001```
* Abrir postman y realizar una petición ```POST``` para generar el token de Autenticación en la siguiente dirección ```http://127.0.0.1:5001/gateway/login```
    * En el cuerpo del request indicar la siguiente información:
    {
    "usuario":"Usuario1234",
    "password":"pa55woRd$123"
    }
* Abrir postman y realizar una petición ```POST``` para crear una nueva orden de venta en la siguiente dirección ```http://127.0.0.1:5001/gateway/orden-venta/```
    * Del token generado en el login, copiarlo e pegarlo en la Autorización del Bearer Token de este request.
    * En el cuerpo del request indicar la siguiente información:
    {
        "direccionEnvio":"mi dirección de envío",
        "estado":"CREADO",
        "monto":123456.78,
        "usuario":"Juan Perez"
    }
* Abrir postman y realizar una petición ```PUT``` para crear una nueva orden de venta en la siguiente dirección ```http://127.0.0.1:5001/gateway/orden-venta/[id]```
    * Remplazar [id] con el que devolvió el post.
    * Del token generado en el login, copiarlo e pegarlo en la Autorización del Bearer Token de este request.
    * En el cuerpo del request indicar la siguiente información de actualización:
    {
        "direccionEnvio":"mi dirección de envío nuevo",
        "estado":"CANCELADO",
        "monto":876543.21,
        "usuario":"Juan Perez Sánchez"
    }
* Abrir postman y realizar una petición ```DELETE``` para crear una nueva orden de venta en la siguiente dirección ```http://127.0.0.1:5001/gateway/orden-venta/[id]```
    * Remplazar [id] con el que devolvió el post.
    * Del token generado en el login, copiarlo e pegarlo en la Autorización del Bearer Token de este request.
    * En el cuerpo del request indicar la siguiente información de actualización:
{
    "usuario":"Juan Perez Sánchez"
}

#### Resultados
* Evidencia Autenticación requerida en el Gateway:
<img width="1633" alt="image" src="https://user-images.githubusercontent.com/94886747/226084064-2a905d60-2d7a-4819-9ba2-73fe4b24d9f8.png">

* Creación de orden de venta:
<img width="1633" alt="image" src="https://user-images.githubusercontent.com/94886747/226084347-e1dfaca8-e533-4691-9ea6-10b4dc03a1d1.png">

* Evidencia de creación:
<img width="1366" alt="image" src="https://user-images.githubusercontent.com/94886747/226081969-d7f95fa4-44b8-47ea-b9ae-0e3ffa824cdd.png">

* Evidencia de auditoria:
<img width="1580" alt="image" src="https://user-images.githubusercontent.com/94886747/226082139-fed07b0a-f830-4160-aad7-1dab6c0f2d13.png">
    
* Actualización de orden de venta:
<img width="1633" alt="image" src="https://user-images.githubusercontent.com/94886747/226084386-6a0b4948-9af9-4f26-9a80-d5c6cc4bffc5.png">

* Evidencia de actualización:
<img width="1366" alt="image" src="https://user-images.githubusercontent.com/94886747/226082024-0202e2de-8352-42f1-8238-2806a818df1b.png">

* Evidencia de auditoria:    
<img width="1580" alt="image" src="https://user-images.githubusercontent.com/94886747/226082065-ef77f5b7-7916-4481-8fea-d789a5350c85.png">

* Eliminación de orden de venta:
<img width="1633" alt="image" src="https://user-images.githubusercontent.com/94886747/226084409-64c11319-5b9f-474f-b538-938439e7b257.png">

* Evidencia de eliminación:
<img width="1580" alt="image" src="https://user-images.githubusercontent.com/94886747/226082196-d3343030-df6f-4fd9-bacc-32ae120220fd.png">

* Evidencia de auditoria: 
<img width="1580" alt="image" src="https://user-images.githubusercontent.com/94886747/226082211-6fb2c4c2-d000-4855-b989-39344019d5dd.png">

#### Notas
    
</details>






# Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-

Clonar repositorio:
> git clone https://github.com/CBarreiro22/Sistema_Soporte_Proyecto_CCP-Arquitectura_Agil_Software-

## Ejecucion HU01

Para ejecutar la prueba de historia de usuario se tiene que realizar lo siguiente:

* Crear el ambiente virtual de python ``` python3 -m venv env```
* Instalar las dependencias ```pip install -r requeriments.txt```
* desplegar el microservicio inventario, ingresando dentro del directorio HU01/inventario y desplegar ```flask run```
* desplegar el microservicio producto, ingresando dentro del directorio HU01/producto ```flask run -p 5001```
* desplegar las colas de mensajeria para producto, se ingresa dentro del directorio HU01 y ejecuta el siguiente comando ```celery -A producto.tareas worker  -l info -Q inventario_producto```
* desplegar la cola de monitor , ingresamos al directorio de monitor y ejecutamos el siguiente comando ```celery -A monitor worker -l info``


## Tareas:
Producto
* Crear Modelo producto
  * Parametros de acuerdo al modelo que se definio
* Crear Vista producto
  * Consulta de todos los productos. escribir en la cola
* Crear endpoint
* Crear la cola para leer y escribir mensaje

Inventario
* Crear Modelo Inventario
  * Parametros de acuerdo al modelo que se definio
* Crear Vista inventario
  * Consultar el inventario de todos los productos
  * join con la informacion recogida de productos(el id del producto en el inventario debe existir en producto).
  * return de l informacion recolectada.
* Crear endpoint
* Crear la cola para leer y escribir mensaje

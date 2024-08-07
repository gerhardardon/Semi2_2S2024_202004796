# Proceso ETL
Gerhard Benjamin Ardon Valdez 
202004796

## Introduccion
Se le solicita que realice un proceso de ETL (Extraer, Transformar, Cargar) de los 
archivos  que  se  les  brindaran.  En  base  a  los  archivos  usted  deberá  generar  el 
modelo  que  se  adapte  mejor,  y  posteriormente,  realizar  las  consultas  que  se  le 
soliciten.

## Herramientas utilizadas
-   Python
    - Pyodbc lib
    - Os lib
-   Sql Server
    - Sqlcmd   
    - Docker

## Modelo Datamart
Para esta practica se eligió el modelo estrella debido a su facilidad de implementacion y alta escalabilidad, ademas al no tener tantos campos, no era necesaria la normalizacion de las tablas de dimensiones.

El Modelo Estrella es una técnica de modelado de datos que se utiliza para diseñar y optimizar almacenes de datos y data marts. Su nombre se debe a la forma que tiene el esquema lógico, que consta de una tabla central llamada tabla de hechos y varias tablas periféricas llamadas tablas de dimensiones. Estas tablas se relacionan entre sí mediante claves primarias y foráneas, formando una estructura en forma de estrella.

![Modelo implementado para esta práctica](/Practica1/assets/Modelo.drawio.png)

En donde "Hechos" es la tabla de Hechos, formada mayormente de datos númericos (a excepcion de PassID, que debido al modelo tiene sentido) y las tablas "Pasenger", "Airport", "Country", "Continent" y "Flight" son las dimensiones.

Cada llave priamria cumple su objetivo de llave subrogada para la tabla de hechos.

## Instalacion de sql server con Docker
### Pasos para instalar sql server desde docker 
Descargar la imagen de docker 
```
sudo docker pull mcr.microsoft.com/mssql/server
```
Imiciar el contenedor aceptando todos sus permisos y seteando la nueva contraseña, Ojo la contraseña debe tener 8 caracteres, mayusculas y caracteres especiales o no correra el contenedor 
```
sudo docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=YourPassword123' -p 1433:1433 --name sqlserver -d mcr.microsoft.com/mssql/server
```
Luego verificar con
```
sudo docker ps 
```

### Pasos para acceder a sql server desde consola y ejecutar scripts con sqlcmd
Para acceder a la base de datos se ejecuta el siguiente comando:
```
sqlcmd -S <SERVER> -U <USER> -P <PASSWORD>
```
Para acceder a la base de datos y ejecutar un script en especifico se debe usar:
```
sqlcmd -S <SERVER> -U <USER> -P <PASSWORD> -i <SCRIPT.sql>
```




10/08/2024

## Paralelismo

Se podria definir como la particion de la base de datos para poder procesar de forma paralela distintos discos con distintosm procesadores. Mejora la velocidad en consultas y proporciona "dimensionabilidad" ya que la carga de trabajo puede incrementar pero sin incrementar el tiempo de respuesta.

Existen 4 arquitecturas de de sistemas paralelos:

- Memoria compartida (los procesadores comparten una mem comun)
- Discos compartidos (los proc comparten un conjunto discos comun como raid y jbods)
- Sin compartimiento (no comparten ni mem ni discos)
- Jerarquica (es un hibrido de arq. anteriores)

Existe **Paralelismo de grado grueso** el cual disponiendo de pocos procesadores, estos no intentan dividir las consultas si no que ejecuta cada una posibilitando la concurrencia. Toma los procesadores y ejecuta solamente en uno.

Y tambien el de **grado fino** el cual si divide las consultas entre los procesadores disponibles.

## Optimizacion

Por concepto las operaciones relacionales son optimizables, el termino "optimizacion" como tal es una exageracion ya que debido al cambio de los datos es imposible optimizar de manera absoluta toda la db.

---

14/08/2024

## Procesamiento de consultas para optimizacion

- **Convertir la consulta a su forma interna:** Se convierte la consulta en un aforma mas adecuada para manejar en la maquina, la consulta se empieza a analizar desde el FROM (esta es la entrada a las tablas, ya que define que table se utilizara para la consulta) Se utiliza la forma canónica de la consulta.
- **Encausamiento:** Es la forma de escribir bien las consultas para facilitar el procesamiento de la misma en la db.
-**Optimizacion semantica:** Semanticamente son diferentes pero cualitativamente son iguales a otras sentencias.  

---
21/08/2024
## Estimacion
La estimacion del tamaño del resultado de la operacion depende del predicado de la seleccion (tamaño)

Se debe consultar en WHERE por las condiciones mas determinantes de primero, para realizar "encausamiento" y optimizar más las tablas.

---

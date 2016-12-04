# Control 9

### Forma 1

**(6 pts.) Explique qué tarea cumple y cómo funciona el método `listen()` en un *socket*. ¿Qué argumento(s) recibe y qué significan(n)?**

El método `listen()` permite al *socket* escuchar por potenciales conexiones. El argumento es un número (`int`) que corresponde al número máximo de conexiones pendientes permitidas (es decir, no aceptadas).

* (4 pts.) Qué hace `listen()`
* (2 pts.) Qué recibe `listen()`

----------

### Forma 2

**(6 pts.) Explique en qué se diferencia la creación de un *socket* usando `SOCK_DGRAM` y `SOCK_STREAM`. Para cada caso escriba un ejemplo donde es recomendable el uso**

Tanto `SOCK_DGRAM` como `SOCK_STREAM` indican tipos de *socket*. Tenemos `SOCK_STREAM` para conecciones **TCP** y `SOCK_DGRAM` para conexiones **UDP**. Como TCP garantiza que los datos van a llegar intactos se utiliza para transmisión de archivos, envío de correos, HTTP, etc. En cambio, UDP permite el envío de datos sin necesidad de establecer una conexión por lo que se utiliza para *streaming* de video y audio, información del clima, juegos *online*, etc.

* (2 pts.) Definir `SOCK_DGRAM`
* (2 pts.) Definir `SOCK_STREAM`
* (1 pts.) Ejemplo para `SOCK_DGRAM`
* (1 pts.) Ejemplo para `SOCK_STREAM`

----------

### Forma 3

**(6 pts.) Explique qué tarea cumple y cómo funciona el método `bind()`. ¿Qué argumento(s) recibe y qué significa(n)?**

El método `bind()` enlaza el *socket* a un puerto dado. El argumento que recibe puede ser una tupla (`tuple`) con la dirección del puerto al que se debe enlazar.

* (4 pts.) Qué hace `bind()`
* (2 pts.) Qué recibe `bind()`

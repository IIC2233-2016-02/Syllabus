A continuación se encuentra documentada toda la API utilizada en esta actividad.

### > GET Inicio - New URL Discovered

Donde http://ac15-aaossa.rhcloud.com/new_url_discovered será la url que es secreta y deben encontrar

```
GET http://ac15-aaossa.rhcloud.com/inicio
GET http://ac15-aaossa.rhcloud.com/new_url_discovered
```
##### Ejemplo de output
```
{
    "lista": [
        "string1",
        "string2",
        "string3",
    ]
}
```

### > POST Inicio - New URL Discovered

```
POST http://ac15-aaossa.rhcloud.com/inicio
POST http://ac15-aaossa.rhcloud.com/new_url_discovered
```
##### Parametros
```
{
	"string": "string_concatenado",
	"username": "nombre_github"
}
```
##### Ejemplo de output
```
{
    "message": "Lo lograste :D Ve a la siguiente url para la siguiente tarea",
    "url": APP_URL + "/********"
}
```

### > POST Last URL
```
POST http://ac15-aaossa.rhcloud.com/last_url
```
##### Parametros
```
{
	"string": "string_concatenado",
	"username": "nombre_github"
}
```
##### Ejemplo de output
```
{
    "message": "Bien hecho! Ahora solo queda la mitad de la AC #ups",
    "password": password
}
```

### > POST Ayudantes - Alumnos
```
POST http://ac15-aaossa.rhcloud.com/ayudantes
POST http://ac15-aaossa.rhcloud.com/alumnos
```
##### Parametros
```
{
	"password": "*********",
	"username": "nombre_github"
}
```
##### Ejemplo de output
```
{
    "nombre_github1": id1,
    "nombre_github2": id2,
    "nombre_github3": id3,
    "nombre_github4": id4
}
```

### > POST Ayudantes - Alumnos
```
POST http://ac15-aaossa.rhcloud.com/ayudantes/<id_ayudante_x>
POST http://ac15-aaossa.rhcloud.com/alumnos/<id_alumno_x>
```
##### Parametros
```
{
	"password": "*********",
	"username": "nombre_github"
}
```
##### Ejemplo de output
```
[1,0,2,1,0,0....]
```


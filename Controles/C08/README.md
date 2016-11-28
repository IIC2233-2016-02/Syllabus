# Control 8

### Forma 1

**(6 pts.) Explique qué ocurre, paso a paso, cuando se ocupa el parámetro `cls` de `json.dump`.**

Para ocupar el parámetro `cls` de `json.dump` se debe utilizar una sub-clase de `json.JSONEncoder`**(1 pts)**.
Durante la serialización de un objeto, la información a serializar se obtendrá aplicando el método `default` de las instancias de la clase entregada sobre el objeto en cuestión **(2 pts)**.
La información retornada tras la correcta ejecución de `default`, suponiendo que dicha información es serializable sin ambigüedades, será llevada a formato JSON como corresponde **(2 pts)**.
La cadena JSON resultante será escrita en el archivo indicado como parámetro al momento de su ejecución **(1 pto)**.

----------

### Forma 2

**(6 pts.) Explique para qué sirve implementar el método `__getstate__` en una clase cualquiera de Python.**

Personalizar la serialización de un objeto **(3 pts)** mediante `pickle.dump(s)` **(3 pts)**.

----------

### Forma 3

**(6 pts.) Explique para qué sirve implementar el método `__setstate__` en una clase cualquiera de Python.**

Personalizar la deserialización de un objeto **(3 pts)** mediante `pickle.load(s)` **(3 pts)**.
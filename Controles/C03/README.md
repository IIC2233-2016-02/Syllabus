# Control 3

### Forma 1

**1) (2 pts.) ¿Que elementos se seleccionarán de la lista "```b```" al ejecutar ```b[::-a]```?**

Se seleccionan todos aquellos elementos desde el final hacia el inicio de la lista en pasos de tamaño a. Por ejemplo:

```python
b = [1, 2, 3, 4, 5]
>>> b[::-2]
[5, 3, 1]
>>> b[::-3]
[5, 2]
```
Responde correctamente **(2 pts)**

**2) (4 pts.) Escriba una función en python que permita recorrer recursivamente un árbol binario e imprimir el valor de cada nodo según la secuencia hijo izquiera-padre-hijo derecha.**

```python
def recorrer(self):
    id_derecha = None if self.hijo_derecho is None else self.hijo_derecho.id
    id_izquierda = None if self.hijo_izquierdo is None else self.hijo_izquierdo.id

    print("id hijo izquierda: {0} - id padre: {1} - id hijo derecha: {2}".format(id_izquierda,
    	self.id, id_derecha))

    for hijo in (self.hijo_izquierdo, self.hijo_derecho):
        if hijo is not None:
            hijo.recorrer()
```
Define recursión **(1 pto)**
Abarca casos límites **(1 pto)**
Imprime en el orden correcto **(1 pto)**
Por hacer un ejemplo de código bien escrito, i.e que sea coherente y cumpla con la sintaxis de Python **(1 pto)**

----------

### Forma 2
**1) (2 pts.) Explique que ocurre con la lista "```d```" al ejecutar ```d[::-1]```.**

Se seleccionan todos los elementos de la lista d en orden inverso. Por ejemplo:

```python
d = [1, 2, 3, 4, 5]
>>> d[::-1]
[5, 4, 3, 2, 1]
```

Responde correctamente **(2 pts)**

**2) (4 pts.) Escriba una función en python que permita recorrer recursivamente un árbol binario e imprimir el valor de cada nodo según la secuencia hijo izquiera-hijo derecha-padre.**

```python
def recorrer(self):
    id_derecha = None if self.hijo_derecho is None else self.hijo_derecho.id
    id_izquierda = None if self.hijo_izquierdo is None else self.hijo_izquierdo.id

    print("id hijo izquierda: {0} - id hijo derecha: {1} - id padre: {2}".format(id_izquierda,
    	id_derecha, self.id))

    for hijo in (self.hijo_izquierdo, self.hijo_derecho):
        if hijo is not None:
            hijo.recorrer()
```
Define recursión **(1 pto)**
Abarca casos límites **(1 pto)**
Imprime en el orden correcto **(1 pto)**
Por hacer un ejemplo de código bien escrito, i.e que sea coherente y cumpla con la sintaxis de Python **(1 pto)**

----------

### Forma 3
**1) (2 pts.) ¿Que elementos se seleccionarán de la lista "```a```" al ejecutar ```a[:-d]```? Escriba un ejemplo.**

Se seleccionan todos los elementos desde el índice 0 hasta el índice len(a)-d (no inclusive). Por ejemplo:

```python
a = [1, 2, 3, 4, 5]
>>> a[::-2]
[5, 3, 1]
>>> a[::-3]
[4, 1]
```

Responde correctamente **(1 pto)**
Da un buen ejemplo **(1 pto)**

**2) (4 pts.) Escriba una función en python que permita recorrer recursivamente un árbol binario e imprimir el valor de cada nodo según la secuencia padre-hijo izquiera-hijo derecha.**

```python
def recorrer(self):
    id_derecha = None if self.hijo_derecho is None else self.hijo_derecho.id
    id_izquierda = None if self.hijo_izquierdo is None else self.hijo_izquierdo.id

    print("id padre: {0} - id hijo izquierda: {1} - id hijo derecha: {2}".format(self.id, 
    	id_izquierda, id_derecha))

    for hijo in (self.hijo_izquierdo, self.hijo_derecho):
        if hijo is not None:
            hijo.recorrer()
```

Define recursión **(1 pto)**
Abarca casos límites **(1 pto)**
Imprime en el orden correcto **(1 pto)**
Por hacer un ejemplo de código bien escrito, i.e que sea coherente y cumpla con la sintaxis de Python **(1 pto)**

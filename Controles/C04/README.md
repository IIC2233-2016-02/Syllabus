# Control 4

### Forma 1

**(6 pts.) ¿Qué resultado imprimen las sentencias `print` en el siguiente código Python?**
```python
class Aux:
	def __init__(self, a, b):
		self.a = a
		selg.b = b
		
	def __repr__(self):
		return '{} - {}'.format(self.a, self.b)


def bar(l):
	l.b += 1
	return l


foo = [Aux(a, b) for a, b in zip(range(3), range(3))]
print(foo)

r = list(map(bar, filter(lambda x: x.a % 2 == 0, foo)))
print(r)

print(foo)
```

La sentencias `print` imprimen:
```python
[0 - 0, 1 - 1, 2 - 2]  # print(foo)
[0 - 2, 2 - 4]  # print(r) 
[0 - 2, 1 - 1, 2 - 4]  # print(foo)
```

`foo` es solo una lista por comprensión de objetos `Aux` construidos a partir de los valores entregados por `zip(range(3), range(3))`, para ser exactos, las tuplas `(0, 0), (1, 1), (2, 2)`. Cuando una lista es impresa se utilizan las representaciones de los elementos que contiene **(2 pts)**.

`r` es la lista de objetos `Aux` obtenida tras aplicar `bar` a los objetos en `foo` cuyos atributos `a` fuesen par **(2 pts)**.

`map` utiliza la función `bar`, la cual modifica los atributos de los objetos que recibe. Esos cambios se verán reflejados en la última impresión de `foo` ya que en Python todo se entrega por referencia **(2 pts)**.

Se descuentan **0.25 pts** por cada impresión en la que el alumno demuestre no comprender del todo el método `format` de las cadenas en Python, consiguiendo una impresión no del todo correcta.

----------

### Forma 2
**(6 pts.) ¿Qué resultado imprime la sentencia `print` como salida del siguiente código Python?**
```python
p = [['0001', 'A', 2, 1000],
	 ['0002', 'B', 3, 3000],
	 ['0003', 'C', 20, 200]]
	 
o = (3, 0.9)

t = list(map(lambda x: (x[0], x[2]) if x[1] != o[0] else (x[0], x[2] * o[1]), map(lambda x: (x[0], x[2], x[2] * x[3]), p)))

m = reduce(lambda a, b: a if (a > b) else b, map(lambda x: x[1], t))

print(m)
```

La sentencia `print` imprime:
```python
8100.0
```

`t` es una lista obtenida mediante funciones `map`:
```python
[('0001', 2000), ('0002', 8100.0), ('0003', 4000)]
```
Se requiere un buen entendimiento de `lambda`, `map` y qué resulta de aplicar `list` sobre un generador **(3 pts)**.

`m` es el resultado de obtener el máximo valor en `map(lambda x: x[1], t)`. Se requiere un buen entendimiento de `lambda` y `reduce` **(3 pts)**.

En caso de que el alumno no consiga el resultado esperado pero demuestre un dominio parcial sobre la rama funcional que ofrece Python se le otorgará parte del puntaje.

----------

### Forma 3
**(6 pts.) ¿Qué resultado imprime la sentencia `print` al final del siguiente código Python?**
```python
def ar(*args):
	et = yield
	xt1 = 0
	xt2 = 0
	while True:
		xt = (xt1 * args[0] + xt2 * args[1] + et + args[2])
		xt2 = xt1
		xt1 = xt
		et = yield xt


n = [1, 2, 3]
m = ar(-1.0, 1.0, 1.0)
m.send(None)
y = [m.send(i) for i in n]

print(y)
```

La sentencia `print` imprime:
```python
[2.0, 1.0, 5.0]
```

El alumno debe comprender que el primer parámetro enviado es `None` ya que un generador recién iniciado no puede recibir algo distinto **1 pto**.

Tener un buen entendimiento de cómo funciona `yield` para recibir **2 pts** e enviar **2 pts** parámetros al generador, además de la función del bloque `while` en el código **1 pto**.
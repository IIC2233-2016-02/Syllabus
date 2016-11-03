# Forma 1

Un objeto será compartido concurrentemente entre varios `threads`. Re-escriba el código a continuación para que esto sea posible.

```python
class MiObjeto:
    def __init__(self, valor=0):
        self._valor = valor
    def incr(self, delta=1):
        self._valor += delta
    def decr(self, delta=1):
        self._valor -= delta
```

## Solución
Las instrucciones de la forma `self._valor += delta` representan en verdad dos operaciones, una de lectura y una de escritura:
```
v = self._valor
self._valor = v + delta
```
Dado a que se espera que este proceso sea atómico, es necesario usar un `lock` para que una vez que comience una de estas modificaciones, se termine sin que otro `thread` altere el proceso.

Luego, el código correcto será el que sigue:

```python
class MiObjeto:
    def __init__(self, valor=0):
        self._valor = valor
        self._lock = threading.Lock()
    def incr(self, delta=1):
        with self._lock:
            self._valor += delta
    def decr(self, delta=1):
        with self._lock:
            self._valor -= delta
```
Notar que el `lock` pertenece a cada una de las instancias de `MiObjeto` y **no** a la clase.

## Puntaje
  - **2 pts** por instanciar el `lock` de forma correcta
    (**1 pto** si se instancia en un lugar inadecuado)
  - **2 pts** por utilizar el correctamente el `lock` en `self._valor += delta`
    (**1 pto** si se intenta, pero se utiliza de forma incorrecta)
  - **2 pts** por utilizar correctamente el `lock` en `self._valor -= delta`
    (**1 pto** si se intenta, pero se utiliza de forma incorrecta)

# Forma 2
Explique qué ocurre en el siguiente código. Escriba lo que imprimiría. Si hay distintos *outputs* posibles, escríbalos.

```python
def f1(lock1, lock2):
    with lock1:
        print('Primera parte')
        time.sleep(10)
    with lock2:
        print('Segunda parte')
        time.sleep(5)


def f2(lock1, lock2):
    with lock2:
        print('Primera parte')
        time.sleep(10)
    with lock1:
        print('Segunda parte')
        time.sleep(5)


a_lock = threading.Lock()
b_lock = threading.Lock()

t1 = threading.Thread(target=f1, args=(a_lock, b_lock))
t2 = threading.Thread(target=f2, args=(a_lock, b_lock))

t2.start()
t1.start()
```
## Solución
El thread *t2* se apropiará del lock *b_lock* e imprimirá "Primera parte". El thread *t1* se apropiará de *a_lock* y ejecutará su código que imprimirá también "Primera parte". Luego del *time.sleep(10)* de *t2*, se liberará *b_lock*, y para *t1*, luego de su *time.sleep(10)*, se liberará *a_lock*, por lo que *t2* podrá apropiarse de él en la segunda parte e imprimirá "Segunda parte", y a su vez, *t1* se apropiará de *b_lock* e imprimirá también "Segunda parte".

El *output* es único y será el siguiente:
```
Primera Parte
Primera Parte
Segunda Parte
Segunda Parte
```

## Puntaje

  - **3 pts** por explicar lo que ocurre.
  - **3 pts** por escribir lo que imprimiría.


# Forma 3
Explique qué ocurre en el siguiente código. Escriba lo que imprimiría. Si hay distintos *outputs* posibles, escríbalos.

```python
def f1(lock1, lock2):
    with lock1:
        print('Primera parte')
        time.sleep(10)
        with lock2:
            print('Segunda parte')
            time.sleep(5)


def f2(lock1, lock2):
    with lock2:
        print('Primera parte')
        time.sleep(10)
        with lock1:
            print('Segunda parte')
            time.sleep(5)


a_lock = threading.Lock()
b_lock = threading.Lock()

t1 = threading.Thread(target=f1, args=(a_lock, b_lock))
t2 = threading.Thread(target=f2, args=(a_lock, b_lock))

t2.start()
t1.start()
```

## Solución
El thread *t2* se apropiará del lock *b_lock* e imprimirá "Primera parte". El thread *t1* se apropiará de *a_lock* y ejecutará su código que imprimirá también "Primera parte". Al momento que *t2* intente adquirir *a_lock*, no podrá continuar ejecutando su código pues el lock ya está bloqueado por *t1*, y a su vez, *t1* tampoco puede seguir con su código ya que *b_lock* está bloqueado por el thread *t2*. Por lo tanto, el programa quedará en un *dead-lock*.

El *output* es único y será el siguiente:
```
Primera Parte
Primera Parte
```

## Puntaje

  - **3 pts** por explicar lo que ocurre.
  - **3 pts** por escribir lo que imprimiría.



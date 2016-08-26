from random import randint
from collections import namedtuple


def metodo_tuplas():
    'Metodo que retorna una tupla con 3 numeros aleatorios: '
    return randint(0, 9), randint(10, 99), randint(100, 999)


def metodo_named():
    'Metodo que retorna una namedtuple de un triangulo,  con sus catetos 1 y 2 y la hipotenusa'
    Triangulo = namedtuple('Triangulo', 'cateto1 cateto2 hipotenusa')
    return Triangulo(3, 4, 5)


unidad, decena, centena = metodo_tuplas()  # Puedo guardar los tres elementos de la tupla por separado
numeros = metodo_tuplas()  # O puedo guardarlo como una tupla,  directamente

# Aca vemos como se imprimen los distintos resultados
print(numeros)
print(unidad)
print(decena)
print(centena)

# Una tupla es inmutable, no puedo setear sus valores!
# numeros[1] = 28  # Si descomentas esta linea podras ver el error al tratar de setear un valor
print(numeros[1])

tri = metodo_named()
# tri es una namedtuple, puedo ver sus componentes llamandolos directamente

# Son dos formas de imprimir, pero muestran lo mismo
print('Triangulo rectangulo de lados {0.cateto1}, {0.cateto2} y {0.hipotenusa}'.format(tri))
print('Triangulo rectangulo de lados {}, {} y {}'.format(tri.cateto1, tri.cateto2, tri.hipotenusa))

# Tambien los puedo ver utilizando el indice en que fueron ingresados en el namedtuple
# Al llamar al [1], nos muestra cateto2
print(tri[1])

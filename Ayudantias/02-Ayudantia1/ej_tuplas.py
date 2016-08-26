from random import randint
from collections import namedtuple

def metodo_tuplas():
    return randint(0,9), randint(10,99), randint(100, 999)

def metodo_named():
    Triangulo = namedtuple('Triangulo', 'cateto1 cateto2 hipotenusa')
    return Triangulo(3, 4, 5)


unidad, decena, centena = metodo_tuplas()  # Lo guardo como cada una de sus componentes
numeros = metodo_tuplas()  # Lo guardo en la tupla

print(numeros)
print(unidad)
print(decena)
print(centena)

# numeros[1] = 28
print(numeros[1])

a = 'Triangulo'
tri = metodo_named()
print('{1} rectangulo de lados {0.cateto1}, {0.cateto2} y {0.hipotenusa}'.format(tri, a))

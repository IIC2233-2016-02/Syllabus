'''
class Perro:
    instancias = []

    def __new__(cls, *args, **kwargs):
        print(args, kwargs)
        args = ('Idea of Harambe', )
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print(args, kwargs)
        Perro.instancias.append(self)

    def __call__(self):
        print('¡Guau!')


perro = Perro('Harambe')
print(Perro.instancias)
perro()
'''
#==============================================================================
class Almacenador(type):
    instancias = []

    def __init__(cls, *args, **kwargs):
        print('¡Instancia de la clase Almacenador creada!')
        Almacenador.instancias.append(cls)
        return super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        print('¡Instancia de la clase Almacenador llamada!')
        return super().__call__(*args, **kwargs)


class Perro(metaclass=Almacenador):
    pass


Perro()


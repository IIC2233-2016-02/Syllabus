class AddressHolder:

    def __init__(self, calle='', ciudad='', numero='', comuna='',**kwargs):
        print('Adress:')
        print(kwargs)
        super().__init__(**kwargs)
        self.calle = calle
        self.ciudad = ciudad
        self.comuna = comuna
        self.numero = numero

class Persona:

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Contacto(Persona):

    def __init__(self, nombre = '', email = '', **kwargs):
        print('Contacto:')
        print(kwargs)
        super().__init__(**kwargs)
        self.nombre = nombre
        self.email = email

class Cliente(Contacto, AddressHolder):

    def __init__(self, telefono='', nombre='', **kwargs):
        print('Cliente:')
        print(kwargs)
        super().__init__(nombre=nombre, **kwargs)
        self.telefono = telefono

print(Cliente.__mro__)

c = Cliente(nombre = 'Juan Perez', email = 'jp@gmail.com', telefono = '23542331',
            calle = 'Pedro de Valdivia', numero = '231', comuna = 'Providencia', ciudad = 'Santiago')


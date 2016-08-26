class Contacto:

    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Cliente(Contacto):

    def __init__(self, telefono, nombre, email):
        super().__init__(nombre, email)
        self.telefono = telefono

client = Cliente(27291673, 'Anders', 'mail@uc.cl')
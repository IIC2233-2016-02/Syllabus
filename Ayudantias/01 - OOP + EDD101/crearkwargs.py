class Contacto:

    def __init__(self, nombre, email, **kwargs):
        self.nombre = nombre
        self.email = email

class Cliente(Contacto):

    def __init__(self, telefono, **kwargs):
        super().__init__(**kwargs)
        self.telefono = telefono

client = Cliente(telefono=27291673, nombre='Anders', email='mail@uc.cl', direccion=10)
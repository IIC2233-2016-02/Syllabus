class Clase:
    atributo_clase = 6

    def __init__(self):
        self.atributo_objeto = 8

    def metodo_objeto(self, arg1, arg2):
        self.atributo_objeto = arg1 * arg2

    @classmethod
    def metodo_clase(cls, arg1, arg2):
        cls.atributo_clase = arg1 * arg2


if __name__ == '__main__':
    objeto1 = Clase()
    objeto2 = Clase()
    print(Clase.atributo_clase)  # 6
    Clase.metodo_clase(4, 6)
    print(Clase.atributo_clase)  # 24
    print(objeto2.atributo_clase)  # 24
    objeto1.metodo_objeto(3, 5)
    print(objeto1.atributo_objeto)  # 15
    print(objeto2.atributo_objeto)  # 8

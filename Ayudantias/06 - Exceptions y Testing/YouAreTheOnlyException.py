class ErrorBrigi2(Exception):
    pass


class ErrorCuantico(Exception):

    def __init__(self, a):
        # sobre escribimos el __init__ para cambiar el ingreso de los parmetros
        super().__init__(
            "El/La ayudante {0} no suficientemente bacan".format(a))


class Selector:

    @staticmethod
    def escoger_ayudante(nombre):
        try:
            mentores = ["Freddie", "Freddie2(aka Benjamin)", "Flooryh", "Cote"]

            if nombre not in mentores:
                raise ErrorBrigi2(
                    "El ayudante debe ser un mentor :(")      # Funciona sin parentesis
                											  # Si no se pone nada, no se imprime nada
            if nombre != "Freddie":
                raise ErrorCuantico(nombre)

            # return 2 / 0

        except ErrorCuantico as e:
            print("Error {}".format(e))

        except ErrorBrigi2 as e:
            print("Error {}".format(e))

        # except ZeroDivisionError as err:
        #     print(type(err))


selector = Selector()
selector.escoger_ayudante("Juan")
selector.escoger_ayudante("Flooryh")
# selector.escoger_ayudante("Freddie")


# Descomentar todas las lineas comentadas para mostrar lo que imprime un
# error normal de python

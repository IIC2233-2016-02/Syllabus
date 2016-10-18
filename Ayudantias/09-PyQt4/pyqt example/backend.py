from random import random
from PyQt4 import QtGui
from PyQt4 import QtCore
from  time import sleep

# Esta clase es un evento personalizado,
# para enviar informacion en una senhal
class MoveMyImageEvent:
    """
    Las instancias de esta clase
    contienen la informacion necesaria
    para que la ventana actualice
    la posicion de la imagen
    """

    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y


# Esta clase (que es un thread) corresponde al backend de la aplicacion
class Vehicle(QtCore.QThread):
    trigger = QtCore.pyqtSignal(MoveMyImageEvent)
    # pyqtSignal recibe *args que le indican
    # cuales son los tipos de argumentos que seran enviados
    # en este caso, solo se enviara un argumento:
    #   objeto clase MoveMyImageEv
    # TENDRIA MAS SENTIDO QUE ESTE ATRIBUTO NO FUESE ESTATICO?
    #   Intentenlo en casa...
    #   spoiler: PyQt4-KHEEE?

    def __init__(self, parent, path, x, y, wait):
        """
        Un Vehicle es un QThread que movera una imagen
        en una ventana. El __init__ recibe los parametros:
            parent: ventana
            x e y: posicion inicial en la ventana
            wait: cuantos segundos esperar
                antes de empezar a mover su imagen
        """
        super().__init__()
        self.image = QtGui.QLabel(parent)
        self.path = path
        self.image.setPixmap(QtGui.QPixmap(path).scaled(64, 64, QtCore.Qt.KeepAspectRatio))
        self.image.show()
        # self.image.setVisible(True)
        self.trigger.connect(parent.actualizarImagen)
        self.__position = (0, 0)
        self.lag = wait

        # esta linea se ve inocente
        # pero va a mandar una senhal (evento) a la ventana
        self.position = (x, y)

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

        # El trigger emite su senhal a la ventana
        self.trigger.emit(MoveMyImageEvent(
            self.image, self.position[0], self.position[1]
        ))

        # Prueben cambiar las lineas anteriores
        # por lo siguiente (para que el thread mueva
        # directamente la label "self.imagen")
        # self.image.move(self.position[0], self.position[1])

    def hide(self):
        self.image.hide()

    def run(self):
        self.active = True
        sleep(self.lag)  # Cuanto tardara en partir
        while self.active:
            x, y = self.position
            self.position = (x+random(), y)
            if self.position[0] >= 350:
                self.active = False
            sleep(0.01)

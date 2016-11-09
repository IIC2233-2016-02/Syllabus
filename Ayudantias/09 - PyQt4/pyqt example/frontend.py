"""Editado de IIC2233-2016-1"""
from PyQt4 import QtGui
from PyQt4 import QtCore
import backend as BE


# Esta clase corresponde a la ventana, es decir al frontend de la aplicacion
class Ventana(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.__setUp()

    def __setUp(self):
        self.setGeometry(100, 100, 450, 250)
        self.setWindowTitle("Car race")

        self.start_boton = QtGui.QPushButton('&Start', self)
        self.start_boton.clicked.connect(self.start)
        self.start_boton.move(275, 210)

        self.restart_boton = QtGui.QPushButton('&Restart', self)
        self.restart_boton.clicked.connect(self.restart)
        self.restart_boton.move(275, 210)


        self.restart_boton.hide()


    def start(self):
        self.car_creation()
        self.start_boton.hide()
        self.restart_boton.show()

    def restart(self):
        """
        Aca es necesario eliminar los autos que ya existen primero, es dificil borrar
        un qthread sin que el programa deje de funcionar
        """
        for car in self.cars:
            car.active = False
            car.hide()
            car.terminate()
            car.wait()
            # car.quit()
            # car.exit()
            car.deleteLater()
        self.car_creation()

    def car_creation(self):
        # Creamos 1 thread por cada auto
        # que iran moviendo las imagenes
        # notar que empezaran almismo tiempo, pero podemos cambiar el wait
        # de cada uno para que partan en distintos tiempos
        colors = ['Yellow.png', 'Orange.png', 'Cyan.png', 'Green.png', 'Red.png']
        self.cars = list()
        for i in range(len(colors)):
            _path = colors[i]
            car = BE.Vehicle(
                parent=self,
                path=_path,
                x=0, y=i*40,
                wait= 0  # Podemos cambiar esto para que no partan al mismo tiempo
            )
            self.cars.append(car)
            car.start()

    # La sintaxis es igual que para los
    # ejemplos en el item anterior
    # esto recibira un objeto clase MoveMyImageEvent
    def actualizarImagen(self, myImageEvent):
        label = myImageEvent.image
        label.move(myImageEvent.x, myImageEvent.y)

if __name__ == '__main__':
    app = QtGui.QApplication([])
    ventana = Ventana()
    ventana.show()    
    app.exec_()

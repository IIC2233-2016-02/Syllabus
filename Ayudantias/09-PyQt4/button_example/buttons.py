"""Tipos de botones"""
from PyQt4 import QtGui
from PyQt4 import QtCore


class MarioBlock(QtGui.QPushButton):
    def __init__(self, path, *args):
          super().__init__(*args)
          self.setStyleSheet("background-image: url(retroblock.png)")
          self.setFixedWidth(85)
          self.setFixedHeight(85)



class Ventana(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.__setUp()

    def __setUp(self):
        for i in range(3):
            boton = QtGui.QPushButton(str(i), self)
            boton.move(100*i, 0)
            boton.clicked.connect(self.boton_clickeado)

        # Normalmente, uno querria guardar este tipo de botones para
        # verificar circle.isChecked(), lo mismo con los square
        for i in range(3):
            circle = QtGui.QRadioButton(str(i), self)
            circle.move(120*i, 30)

        for i in range(3):
            square = QtGui.QCheckBox(str(i), self)
            square.move(120*i, 60)

        for i in range(3):
            block = MarioBlock('retroblock.png', '', self)
            block.move(160 * i, 100)
            block.clicked.connect(self.mario_hit)

        self.move(400, 300)


    def boton_clickeado(self):
        # En este método identificaremos el botón

        # Sender retorna el objeto que fue clickeado
        boton = self.sender()

        # Actualizamos
        print('Button: {}'.format(boton))

    def mario_hit(self):
    	# Primero obtengo el block golpeado
    	block = self.sender()

    	# Cambio su imagen
    	block.setStyleSheet("background-image: url(hit.png)")

    	# Luego de golpearlos no se pueden usar
    	block.setEnabled(False)


if __name__ == '__main__':
    app = QtGui.QApplication([])
    ventana = Ventana()
    ventana.show()    
    app.exec_()

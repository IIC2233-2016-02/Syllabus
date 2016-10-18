"""Ejemplo de layouts"""
from PyQt4 import QtGui
from PyQt4 import QtCore


class Cellphone(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.__setUp()

    def __setUp(self):
        self.label1 = QtGui.QLabel('+ ', self)
        self.label2 = QtGui.QLabel('Ingrese numero ', self)

        # Creamos la grilla para ubicar los Widget (botones) de manera matricial
        self.grilla = QtGui.QGridLayout()

        valores = ['1', '2', '3',
                   '4', '5', '6',
                   '7', '8', '9',
                   '*', '0', '#']

        # Generamos las posiciones de los botones en la grilla y le asociamos
        # el texto que debe desplegar cada boton guardados en la lista valores

        posicion = [(i,j) for i in range(4) for j in range(3)]

        for posicion, valor in zip(posicion, valores):
            if valor == '':
                continue

            boton = QtGui.QPushButton(valor)

            # A todos los botones les asignamos el mismo slot o método
            boton.clicked.connect(self.boton_clickeado)

            # El * permite convertir los elementos de la tupla como argumentos
            # independientes
            self.grilla.addWidget(boton, *posicion)

        llamar = QtGui.QPushButton('&Llamar')
        llamar.clicked.connect(self.boton_llamar)
        borrar = QtGui.QPushButton('&Borrar')
        borrar.clicked.connect(self.boton_borrar)
        colgar = QtGui.QPushButton('&Colgar')
        colgar.clicked.connect(self.boton_colgar)

        # Grilla horizontal para los botones de llamar y colgar
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(llamar)
        hbox.addWidget(borrar)
        hbox.addWidget(colgar)

        # Cambiar los valores segun la separacion de la grilla que se quiera
        self.grilla.setVerticalSpacing(5)
        self.grilla.setHorizontalSpacing(5)
        vbox = QtGui.QVBoxLayout()

        # Agregamos el label al layout con addWidget
        vbox.addWidget(self.label1)
        vbox.addWidget(self.label2)

        # Agregamos el layout de la grilla al layout vertical con addLayout
        vbox.addLayout(self.grilla)
        self.setLayout(vbox)

        # Por ultimo, agregamos la grilla con opciones de llamar/cortar
        vbox.addLayout(hbox)

        self.move(300, 150)  # Muevo la pantalla principal
        self.setWindowTitle('PrograPhone')
        #self.show()

    def boton_clickeado(self):
        # En este método identificaremos el botón

        # Sender retorna el objeto que fue clickeado
        boton = self.sender()

        # Actualizamos
        self.label1.setText('{}{}'.format(self.label1.text(), boton.text()))

    def boton_llamar(self):
        self.label2.setText('Llamando {}'.format(self.label1.text()))

    def boton_colgar(self):
        self.label1.setText('+ ')
        self.label2.setText('Ingrese numero ')

    def boton_borrar(self):
        self.label1.setText(self.label1.text()[0:-1])

if __name__ == '__main__':
    app = QtGui.QApplication([])
    ventana = Cellphone()
    ventana.show()    
    app.exec_()

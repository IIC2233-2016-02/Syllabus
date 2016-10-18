from PyQt4 import QtGui, uic

# Cargamos la interfaz creada mediante QTDesigner
formulario = uic.loadUiType("mainwindow1.ui")
print(formulario[0], formulario[1])

# Creamos nuestra ventana heredando desde la clase base en que se contruyo
# la interfaz en QT-Designer

class MainWindow(formulario[0], formulario[1]):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # Inicializamos la interfaz creada en Qt-Designer


if __name__ == '__main__':
    app = QtGui.QApplication([])
    form = MainWindow()
    form.show()
    app.exec_()
from PyQt4 import QtGui

class MiFormulario(QtGui.QWidget):
    
    def __init__(self):
        super().__init__()
        # Definimos la geometría de la ventana. 
        self.setGeometry(200, 100, 300, 300) 
        
        # Titulo
        self.setWindowTitle('Window')

        # Label: muestra texto
        self.label1 = QtGui.QLabel('Texto:', self)
        self.label1.move(10, 15)

        # LineEdit: input
        # self.edit1 = QtGui.QLineEdit('', self)
        # self.edit1.setGeometry(45, 15, 100, 20)




if __name__ == '__main__':
    app = QtGui.QApplication([])
    formulario = MiFormulario()    
    formulario.show()
    app.exec_()
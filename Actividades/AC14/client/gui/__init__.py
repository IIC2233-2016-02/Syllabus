from .gui import GUI
from PyQt4 import QtGui

def run(custom_gui):
    app = QtGui.QApplication([])
    gui = custom_gui()
    app.exec_()

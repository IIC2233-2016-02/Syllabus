from .main_window import MainWindow
from PyQt4.QtGui import QApplication


__app = QApplication([])


def run(window):
    window.show()
    __app.exec()

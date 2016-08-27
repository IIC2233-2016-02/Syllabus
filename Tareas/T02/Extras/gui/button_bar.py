from PyQt4.QtGui import QWidget, QPushButton, QLabel, QVBoxLayout, QFileDialog
from PyQt4.QtCore import pyqtSignal


class ButtonBar(QWidget):

    open_click = pyqtSignal(str)
    save_click = pyqtSignal(str)
    pass_click = pyqtSignal()
    count_click = pyqtSignal()
    resign_click = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.__layout = QVBoxLayout()

        self.__result_label = QLabel()
        self.set_result('-')
        self.__layout.addWidget(self.__result_label)

        self.__layout.addStretch(1)

        self.open_button = QPushButton("Abrir")
        self.save_button = QPushButton("Guardar")
        self.pass_button = QPushButton("Pass")
        self.count_button = QPushButton("Count")
        self.resign_button = QPushButton("Resign")
        self.open_button.clicked.connect(self.on_open_click)
        self.save_button.clicked.connect(self.on_save_click)
        self.pass_button.clicked.connect(self.on_pass_click)
        self.count_button.clicked.connect(self.on_count_click)
        self.resign_button.clicked.connect(self.on_resign_click)
        self.__layout.addWidget(self.open_button)
        self.__layout.addWidget(self.save_button)
        self.__layout.addWidget(self.pass_button)
        self.__layout.addWidget(self.count_button)
        self.__layout.addWidget(self.resign_button)

        self.setLayout(self.__layout)

    def set_result(self, text):
        self.__result_label.setText("Resultado: {}".format(text))

    def on_open_click(self):
        path = QFileDialog.getOpenFileName()
        self.open_click.emit(path)

    def on_save_click(self):
        path = QFileDialog.getSaveFileName()
        self.save_click.emit(path)

    def on_pass_click(self):
        self.pass_click.emit()

    def on_count_click(self):
        self.count_click.emit()

    def on_resign_click(self):
        self.resign_click.emit()
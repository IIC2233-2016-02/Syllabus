from .central_widget import CentralWidget
from PyQt4.QtGui import QLabel, QMainWindow, QStatusBar
import string


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.__central_widget = CentralWidget(None)

        self.__board = self.__central_widget.board
        self.__nodes_view = self.__central_widget.nodes_widget

        self.__status_bar = QStatusBar()

        self.setCentralWidget(self.__central_widget)
        self.setStatusBar(self.__status_bar)
        self.setMinimumSize(self.__central_widget.size())

        self.__board.on_click.connect(self.on_piece_click)
        self.__nodes_view.node_click.connect(self.on_point_click)

        self.__central_widget.button_bar.open_click.connect(self.on_open_click)
        self.__central_widget.button_bar.save_click.connect(self.on_save_click)
        self.__central_widget.button_bar.pass_click.connect(self.on_pass_click)
        self.__central_widget.button_bar.resign_click.connect(self.on_resign_click)
        self.__central_widget.button_bar.count_click.connect(self.on_count_click)

        self.__status_bar.showMessage("Juego cargado.")

    def add_piece(self, letter, y, text, color):
        self.__board.add_piece(letter, y, text, color)

    def add_square(self, letter, y, color):
        self.__board.add_square(letter, y, color)

    def remove_piece(self, letter, y):
        self.__board.remove_piece(letter, y)

    def add_point(self, x, y, text, color):
        self.__nodes_view.add_point(x, y, text, color)

    def remove_point(self, x, y):
        self.__nodes_view.remove_point(x, y)

    def add_line(self, cord_1, cord_2, color):
        self.__nodes_view.add_line(cord_1, cord_2, color)

    def remove_line(self, cord_1, cord_2):
        self.__nodes_view.remove_line(cord_1, cord_2)

    def set_result(self, points):
        self.__central_widget.button_bar.set_result(points)

    def on_piece_click(self, letra, y):
        pass

    def on_point_click(self, x, y):
        pass

    def on_open_click(self, path):
        pass

    def on_save_click(self, path):
        pass

    def on_pass_click(self):
        pass

    def on_count_click(self):
        pass

    def on_resign_click(self):
        pass

    def show_message(self, message):
        self.__status_bar.showMessage(message)



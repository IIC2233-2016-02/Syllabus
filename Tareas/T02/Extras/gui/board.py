from PyQt4.QtGui import QLabel, QPixmap, QWidget, QPalette
from PyQt4.QtCore import pyqtSignal, Qt
from .utils import get_asset_path
import string


class GOBoard(QWidget):

    on_click = pyqtSignal(str, int)

    def __init__(self):
        super().__init__()
        self.__background_pixmap = QPixmap(get_asset_path("board.png"))
        self.__background_label = QLabel(self)
        self.__background_label.setPixmap(self.__background_pixmap)
        self.setMinimumSize(self.__background_pixmap.size())
        self.__pieces = {}

    def pixmap_height(self):
        return self.__background_pixmap.height()

    def add_square(self, letter, y, color):
        y -= 1
        letters = list(string.ascii_uppercase)
        letters.remove("I")
        a = letters.index(letter)
        if (letter, y + 1) in self.__pieces:
            print("ERROR: Space {},{} already occupied".format(letter, y + 1))
        else:
            piece = GOSquare(27 + a * 23, self.__background_pixmap.height() - (20 + y * 23), color, self)
            self.__pieces[(letter, y + 1)] = piece
            piece.show()

    def add_piece(self, letter, y, text, color):
        y -= 1
        letters = list(string.ascii_uppercase)
        letters.remove("I")
        a = letters.index(letter)
        if (letter, y + 1) in self.__pieces:
            print("ERROR: Space {},{} already occupied".format(letter, y + 1))
        else:
            piece = GOPiece(23 + a * 23, self.__background_pixmap.height() - (24 + y * 23), text, color, self)
            self.__pieces[(letter, y + 1)] = piece
            piece.show()

    def remove_piece(self, letter, y):
        if (letter, y) in self.__pieces:
            piece = self.__pieces[(letter, y)]
            piece.hide()
            piece.deleteLater()
            del self.__pieces[(letter, y)]
        else:
            print("ERROR: There is no piece at {},{}".format(letter, y))

    def mousePressEvent(self, e):
        x = (e.x() - 27) // 23
        y = (self.__background_pixmap.height() - 20 - e.y()) // 23
        y += 2
        letters = list(string.ascii_uppercase)
        letters.remove("I")
        letra = letters[x]
        if y <= 19 and letra <= "T":
            self.on_click.emit(letra, y)


class GOSquare(QWidget):

    BLACK = "black"
    WHITE = "white"

    def __init__(self, x, y, color, parent):
        super().__init__(parent)
        self.__label = QLabel(self)
        self.__label.setFixedSize(13, 13)
        self.__label.setStyleSheet("border-radius: 10px; background-color: {};".format(color))
        self.move(x, y)


class GOPiece(QWidget):
    BLACK = "black"
    WHITE = "white"

    def __init__(self, x, y, text, color, parent):
        super().__init__(parent)
        self.__label = QLabel(str(text), self)
        palette = QPalette()
        if color == "white":
            palette.setColor(QPalette.Foreground, Qt.black)
            self.setStyleSheet("background-image: url(gui/assets/white_piece.png);")
        else:
            palette.setColor(QPalette.Foreground, Qt.white)
            self.setStyleSheet("background-image: url(gui/assets/black_piece.png);")
        self.__label.setPalette(palette)
        self.__label.setFixedSize(22, 22)
        self.__label.setAlignment(Qt.AlignCenter)
        self.move(x, y)

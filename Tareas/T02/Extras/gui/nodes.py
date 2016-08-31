import math
from PyQt4.QtGui import QWidget, QLabel, QHBoxLayout, QScrollArea, QPalette, QPixmap ,QTransform
from PyQt4.QtCore import Qt, pyqtSignal
from .utils import get_asset_path


class NodesWidget(QWidget):

    node_click = pyqtSignal(int, int)

    def __init__(self):
        super().__init__()

        self.__points = {}
        self.lines = {}
        self.max_height = 0
        self.max_width = 0

    def add_line(self, cord_1, cord_2, color):
        key = tuple(sorted([tuple(cord_1), tuple(cord_2)]))
        x = min(cord_1[0], cord_2[0])
        y = min(cord_1[1], cord_2[1])
        if key in self.lines:
            print("ERROR: Line between {} and {} already added.".format(cord_1, cord_2))
        else:
            line = QLabel(self)
            if color == "white":
                pixmap = QPixmap(get_asset_path("hor_line_white"))
            else:
                pixmap = QPixmap(get_asset_path("hor_line_black"))
            c1 = (30 + cord_1[0]*30, 30 + cord_1[1]*30)
            c2 = (30 + cord_2[0]*30, 30 + cord_1[1]*30)
            length = ((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)**(1/2)
            angle = math.degrees(math.atan2(key[1][1] - key[0][1], key[1][0] - key[0][0]))
            pixmap = pixmap.scaled(length, 5)
            pixmap = pixmap.transformed(QTransform().rotate(angle))
            line.setPixmap(pixmap)
            line.move(30 + x*30, 30 + y*30)
            line.show()
            line.lower()
            self.lines[key] = line

    def remove_line(self, cord_1, cord_2):
        key = tuple(sorted([tuple(cord_1), tuple(cord_2)]))
        if key in self.lines:
            label = self.lines[key]
            label.deleteLater()
            del self.lines[key]
        else:
            print("ERROR: No line between {} and {} to be removed.".format(cord_1, cord_2))

    def add_point(self, x, y, number, color):
        if (x, y) in self.__points:
            print("ERROR: Node's space ({},{}) already occupied".format(x, y))
            return
        label = Node(x, y, number, color, self)
        label.move(20 + x*30, 20+y*30)
        label.show()
        self.__points[(x, y)] = label
        if 45 + y*30 > self.max_height:
            self.setMinimumHeight(45 + y * 30)
            self.max_height = 45 + y*30
        if 45 + x*30 > self.max_width:
            self.setMinimumWidth(45 + x*30)
            self.max_width = 45 + x*30

        label.node_click.connect(self.on_node_click)

    def remove_point(self, x, y):
        if (x, y) in self.__points:
            point = self.__points[(x, y)]
            point.hide()
            point.deleteLater()
            del self.__points[(x, y)]
        else:
            print("ERROR: There's no point at {},{}".format(x, y))

    def on_node_click(self, x, y):
        self.node_click.emit(x, y)


class Node(QLabel):

    node_click = pyqtSignal(int, int)

    def __init__(self, x, y, number, color, parent):
        self.x_cord = x
        self.y_cord = y
        super().__init__(str(number), parent)
        self.color = color
        self.number = number
        palette = QPalette()
        if color == "white":
            palette.setColor(QPalette.Foreground, Qt.black)
            self.setStyleSheet("background-image: url({});".format(get_asset_path("white_piece.png", sep="/")))
        else:
            palette.setColor(QPalette.Foreground, Qt.white)
            self.setStyleSheet("background-image: url({});".format(get_asset_path("black_piece.png", sep="/")))
        self.setPalette(palette)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(22, 22)

    def mousePressEvent(self, e):
        self.node_click.emit(self.x_cord, self.y_cord)

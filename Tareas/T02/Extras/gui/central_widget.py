from .board import GOBoard
from .nodes import NodesWidget
from .button_bar import ButtonBar
from PyQt4.QtGui import QWidget, QHBoxLayout, QLabel, QScrollArea
from PyQt4.QtCore import Qt


class CentralWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.h_box_layout = QHBoxLayout()
        self.setLayout(self.h_box_layout)
        self.board = GOBoard()
        self.nodes_widget = NodesWidget()
        self.button_bar = ButtonBar()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidget(self.nodes_widget)
        self.h_box_layout.addWidget(self.board)
        self.h_box_layout.addWidget(self.scroll_area)
        self.h_box_layout.addWidget(self.button_bar)

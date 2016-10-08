from PyQt4.QtGui import QWidget, QLabel, QPixmap, QFont, QSizePolicy
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import Qt
from .utils import get_asset_path
import string


class MainWindow(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__timer = QTimer(self)
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap(get_asset_path(["background.png"])))
        self.__entities = []
        self.__team_1_label = QLabel("Gold Team 1: 0", self)
        self.__team_1_label.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        # self.__team_1_label.setFixedWidth(600)
        self.__font = QFont("", 20)
        self.__font.setBold(True)
        self.__team_1_label.setStyleSheet("color: yellow;")
        self.__team_1_label.setFont(self.__font)
        self.__team_2_label = QLabel("Gold Team 2: 0", self)
        self.__team_2_label.setStyleSheet("color: yellow;")
        self.__team_2_label.setFont(self.__font)
        # self.__team_2_label.setFixedWidth(600)
        self.__team_2_label.move(self.width() - self.__team_2_label.sizeHint().width(), 0)
        self.__objective_label = QLabel("Objective: None", self)
        self.__font_objective = QFont("", 15)
        self.__font_objective.setBold(True)
        self.__objective_label.setFont(self.__font_objective)
        self.__objective_label.move(self.width()//2 - self.__objective_label.sizeHint().width()//2, 0)

    def startMain(self, main, delay=25):
        self.__timer.timeout.connect(main)
        self.__timer.start(delay)

    def add_entity(self, entity):
        entity.setParent(self)
        entity.show()
        self.__entities.append(entity)

    def set_gold_t1(self, gold):
        self.__team_1_label.setText("Gold Team 1: {}".format(gold))
        self.__team_1_label.setFixedWidth(self.__team_1_label.sizeHint().width())

    def set_gold_t2(self, gold):
        self.__team_2_label.setText("Gold Team 2: {}".format(gold))
        self.__team_2_label.setFixedWidth(self.__team_2_label.sizeHint().width())
        self.__team_2_label.move(self.width() - self.__team_2_label.sizeHint().width(), 0)

    def set_objective(self, objective):
        self.__objective_label.setText("Objective: {}".format(objective))
        self.__objective_label.move(self.width() // 2 - self.__objective_label.sizeHint().width() // 2, 0)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Space:
            print(len(self.__entities))
            print("Testing")

    def setFixedSize(self, *__args):
        super().setFixedSize(*__args)
        self.__team_2_label.move(self.width() - self.__team_2_label.sizeHint().width(), 0)
        self.__objective_label.move(self.width() // 2 - self.__objective_label.sizeHint().width() // 2, 0)



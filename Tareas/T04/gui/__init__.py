from .main_window import MainWindow
from PyQt4.QtGui import QApplication, QWidget


__app = QApplication([])
__main_widget = MainWindow()


def add_entity(entity):
    __main_widget.add_entity(entity)
    entity.move(entity.cord_x, entity.cord_y)


def set_gold_t1(gold):
    __main_widget.set_gold_t1(gold)


def set_gold_t2(gold):
    __main_widget.set_gold_t2(gold)


def set_size(x, y):
    __main_widget.setFixedSize(x, y)


def set_objective(objective):
    __main_widget.set_objective(objective)


def run(main, delay=25):
    __main_widget.show()
    __main_widget.startMain(main, delay)
    # __main_widget.showFullScreen()
    __app.exec()

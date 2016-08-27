from gui import MainWindow, run


class MyWindow(MainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SUPER GO DEL FUTURO")

        self.add_piece("A", 1, 0, "white")
        self.add_piece("A", 2, 0, "black")
        self.add_square("A", 3, "black")
        self.add_square("A", 4, "white")

        self.add_point(0, 0, 1, "white")
        self.add_point(1, 0, 2, "black")
        self.add_point(2, 0, 3, "white")
        self.add_point(3, 0, 4, "black")
        self.add_point(4, 0, 5, "white")
        self.add_point(5, 0, 6, "black")
        self.add_point(6, 0, 7, "white")
        self.add_point(7, 0, 8, "black")
        self.add_point(8, 0, 9, "white")
        self.add_point(9, 0, 10, "black")
        self.add_point(10, 0, 11, "white")
        self.add_point(11, 0, 12, "black")
        self.add_point(12, 0, 13, "white")
        self.add_point(13, 0, 14, "black")
        self.add_point(14, 0, 15, "white")

        self.add_point(1, 1, 2, "black")
        self.add_point(2, 1, 3, "white")
        self.add_point(3, 1, 4, "black")
        self.add_point(4, 1, 5, "white")
        self.add_point(5, 1, 6, "black")
        self.add_point(6, 1, 7, "white")

        self.add_point(2, 2, 3, "white")
        self.add_point(3, 2, 4, "black")
        self.add_point(4, 2, 5, "white")
        self.add_point(5, 2, 6, "black")
        self.add_point(6, 2, 7, "white")
        self.add_point(7, 2, 8, "black")
        self.add_point(8, 2, 9, "white")
        self.add_point(9, 2, 10, "black")
        self.add_point(10, 2, 11, "white")
        self.add_line((6, 2), (5, 1), "black")

    def on_piece_click(self, letter, y):
        # self.remove_piece(letter, y)
        self.add_piece(letter, y, '1', "white")
        self.show_message("Added {},{}".format(letter, y))

    def on_point_click(self, x, y):
        self.remove_point(x, y)

    def on_open_click(self, path):
        print(path)

    def on_save_click(self, path):
        print(path)

    def on_pass_click(self):
        self.remove_line((6, 2), (5, 1))
        print("pass")

    def on_count_click(self):
        print("count")

    def on_resign_click(self):
        print("resign")


if __name__ == '__main__':
    run(MyWindow())

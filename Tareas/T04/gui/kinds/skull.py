from ..entity import Entity


class Skull(Entity):

    def __init__(self, class_, pos=(0, 0), size=(50, 50), hp=100, parent=None):
        super().__init__(["Skull " + class_ + ".png"], size=size, hp=hp, pos=pos, parent=parent)

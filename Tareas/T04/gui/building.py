from .entity import Entity
from .utils import get_asset_path


class Building(Entity):

    def __init__(self, kind, pos=(0, 0), size=(100, 150), hp=100):
        self.k = kind
        self.__in_construction = False
        super().__init__(["buildings", self.k + ".png"], size=size, pos=pos, hp=hp)

    @property
    def in_construction(self):
        return self.__in_construction

    @in_construction.setter
    def in_construction(self, other):
        self.__in_construction = other
        self.updatePixmap()

    def updatePixmap(self):
        if self.in_construction:
            self._base_image = ["buildings",  self.k + "_construccion.png"]
        else:
            self._base_image = ["buildings",  self.k + ".png"]
        super().updatePixmap()

class Temple(Building):

    def __init__(self, god, pos=(0, 0), size=(100, 150), hp=100):
        self.god = god

        super().__init__("templo_" + god, pos=pos, size=size, hp=hp)


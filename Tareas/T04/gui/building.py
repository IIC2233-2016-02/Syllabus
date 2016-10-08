from .entity import Entity
from .utils import get_asset_path


class Building(Entity):

    def __init__(self, kind, pos=(0, 0)):
        self.k = kind
        self.__in_construction = False
        super().__init__(["buildings", self.k + ".png"], [100, 150], pos=pos)

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

    def __init__(self, god, pos=(0, 0)):
        self.god = god

        super().__init__("templo_" + god, pos=pos)


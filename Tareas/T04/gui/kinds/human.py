from ..entity import Entity
import random


class Human(Entity):

    def __init__(self, class_, pos=(0, 0), size=(50, 50), hp=100,parent=None):
        if class_ == "villager":
            if random.randint(0, 1):
                class_ += " 2"
        super().__init__(["Human " + class_ + ".png"], size, hp, pos, parent)

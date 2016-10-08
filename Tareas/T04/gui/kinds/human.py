from ..entity import Entity
import random


class Human(Entity):

    def __init__(self, class_, pos=(0, 0), hp=100,parent=None):
        if class_ == "villager":
            if random.randint(0, 1):
                class_ += " 2"
        super().__init__(["Human " + class_ + ".png"], [50, 50], hp, pos, parent)

import gui
from gui.kinds.human import Human
from gui.kinds.skull import Skull
from gui.kinds.orc import Orc
from gui.building import Building, Temple


class Sim:

    def __init__(self):
        self.unit = Skull("warrior", (20, 30),hp=300, size=(100, 100))
        self.building = Building("barracks", pos=(300, 300), hp=400)
        self.building.health = 300
        self.temple = Temple("pezoa", pos=(700, 500),size=(200, 150))
        self.building.in_construction = True

        self.gold = 0

        gui.add_entity(self.unit)
        gui.add_entity(self.building)
        gui.add_entity(self.temple)

    def tick(self):
        if self.unit.health > 0:
            self.unit.cord_x += 1
            self.unit.cord_y += 0.5
            self.unit.angle += 1
            self.unit.health -= 1

        else:
            gui.set_objective("Hernán ha muerto :(")
            self.unit.show()

        self.gold += 1
        gui.set_gold_t1(self.gold)
        gui.set_gold_t2(self.gold)


sim = Sim()
gui.set_size(1024, 680)
gui.set_objective("Matar a Hernán")
gui.run(sim.tick)

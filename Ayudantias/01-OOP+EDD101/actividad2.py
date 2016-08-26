__author__ = 'Ivania Donoso'

from abc import ABCMeta, abstractmethod


class Mascota(metaclass=ABCMeta):
    def __init__(self, nombre="", color="", sexo="", **kwargs):
        #super().__init__(**kwargs)
        self.nombre = nombre
        self.color = color
        self.sexo = sexo

    @abstractmethod
    def comer(self):
        pass

    @abstractmethod
    def jugar(self):
        pass

    def __repr__(self):
        return "Me llamo {}, soy {} y tengo el pelo {}.".format(self.nombre, self.sexo, self.color)



class Perro(Mascota, metaclass=ABCMeta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def ladrar(self):
        print("Guau!! Guau!!")

    def jugar(self):
        print("Tírame la pelota :)")

    def comer(self):
        print("Mami :) Quiero comeeeerr!!")


class Gato(Mascota, metaclass=ABCMeta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def maullar(self):
        print("Miauuu!! Miauuu!")

    def jugar(self):
        print("Humano, ahora, juguemos.")

    def comer(self):
        print("El pellet es horrible. Dame comida en lata.")


class Personalidad(metaclass=ABCMeta):
    def __init__(self, expresion=1,  **kwargs):
        super().__init__(**kwargs)
        self.jugar_solo = 1
        self.jugar_grupo = 1
        self.comidas_dia = 1
        self.dormir = 12
        self.regaloneo = 1
        self.expresion = expresion

    def get_stats(self):
        return self.dormir, self.jugar_solo, self.jugar_grupo, self.comidas_dia, self.regaloneo

    def recalcular_stats(self):
        self.jugar_solo *= self.expresion
        self.jugar_grupo *= self.expresion
        self.comidas_dia *= self.expresion
        self.dormir *= self.expresion
        self.regaloneo *= self.expresion


class Jugueton(Personalidad, metaclass=ABCMeta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jugar_solo = 1
        self.jugar_grupo = 7
        self.comidas_dia = 4
        self.dormir = 8
        self.regaloneo = 4

    def jugar(self):
        print("Quiero jugar")
        if isinstance(self, Perro):
            Perro.jugar(self)
            self.ladrar()
        else:
            Gato.jugar(self)
            self.maullar()

class Egoista(Personalidad, metaclass=ABCMeta):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.jugar_solo = 5
        self.jugar_grupo = 1
        self.comidas_dia = 4
        self.dormir = 12
        self.regaloneo = 2

    def comer(self):
        print("Quiero comida!!!!!!!!!!")
        if isinstance(self, Perro):
            Perro.comer(self)
            self.ladrar()
        else:
            Gato.comer(self)
            self.maullar()


class GoldenPUC(Jugueton, Perro):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.sexo == "Macho":
            self.expresion *= 1.1
            
        else:
            self.expresion *= 0.9
        print(self.__dict__)
        self.recalcular_stats()


class SiamePUC(Egoista, Gato):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.sexo == "Macho":
            self.expresion *= 1
        else:
            self.expresion *= 1.5
        self.recalcular_stats()


class PUCTerrier(Egoista, Perro):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.sexo == "Macho":
            self.expresion *= 1.2
        else:
            self.expresion *= 1
        self.recalcular_stats()

if __name__ == '__main__':
    animals = list()
    animals.append(GoldenPUC(expresion=0.5, nombre="Mara", color="Blanco", sexo="Hembra"))
    animals.append(GoldenPUC(expresion=0.9, nombre="Eddie", color="Rubio", sexo="Macho"))
    animals.append(SiamePUC(expresion=0.9, nombre="Felix", color="Naranjo", sexo="Hembra"))
    animals.append(PUCTerrier(expresion=0.8, nombre="Betty", color="Café", sexo="Hembra"))

    stats_keys = ['dormir', 'jugar_solo', 'jugar_grupo', 'comer_cada', 'regaloneo']
    stats = dict(zip(stats_keys, [-1, -1, 0, 0, 0]))

    for a in animals:
        print(a)
        print(a.get_stats())
        a.jugar()
        a.comer()
        stats_ = a.get_stats()
        if stats_[0] < stats[stats_keys[0]] or stats[stats_keys[1]] == -1:  # Mínimo tiempo de dormir
            stats[stats_keys[0]] = stats_[0]
        if stats_[1] < stats[stats_keys[1]] or stats[stats_keys[1]] == -1:  # Mínimo tiempo de juego individual
            stats[stats_keys[1]] = stats_[1]
        if stats_[2] > stats[stats_keys[2]]:  # Máximo juego en grupo
            stats[stats_keys[2]] = stats_[2]
        stats[stats_keys[3]] += stats_[3]
        stats[stats_keys[4]] += stats_[4]

    print('STATS')
    print("Tiempo de sueño {:.2f}".format(stats[stats_keys[0]]))
    print("Tiempo de {} {:.2f}".format(stats_keys[1], stats[stats_keys[1]]))
    print("Tiempo de {} {:.2f}".format(stats_keys[2], stats[stats_keys[2]]))
    print("{} {:.2f}".format(stats_keys[3], stats[stats_keys[3]]))

    print("Tiempo de {} {:.2f}".format(stats_keys[4], stats[stats_keys[4]]))
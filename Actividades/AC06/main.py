__author__ = "Juan Cortes, Cristian Cortes, Manuel Silva"


# CREA LOS DECORADORES ARRIBA
# DESDE AQUI HACIA ABAJO NO PUEDES MODIFICAR NINGUNA DE LAS CLASES Y FUNCIONES, SOLO DECORARLAS
class Pokedex:
    def __init__(self):
        self.pokemon = list()

    def add_pokemon(self, pokemon):
        self.pokemon.append(pokemon)

    def compare(self):
        print('El mas fuerte es {0.nombre}'.format(
            max(self.pokemon, key=lambda x: len(x.nombre))))

    def __str__(self):
        return 'Llevas {} Pokemon:\n{}'.format(len(self.pokemon), self.pokemon)


class Pokemon:
    def __init__(self, nombre, level, evolutions, owner):
        self.nombre = nombre
        self.level = level
        self.evolutions = evolutions
        self.owner = owner

    def set_attributes(self, tipo):
        self.tipo = tipo

    def __repr__(self):
        return 'Hola soy Charmander!'


class Legendario(Pokemon):
    def __init__(self, *args):
        super().__init__(*args)


if __name__ == '__main__':
    try:
        pik = Pokemon('Pikachu', 32.4, ['Raichu'], 'Ash')
    except Exception:
        print('Su verify parece funcionar :)')

mag = Pokemon('Magikarp', 5, ['Gyarados'], 'Ash')
leg = Legendario('Mew', 80, [], 'Prof. Oak')
pokedex = Pokedex()

pokedex.add_pokemon('Charmander')

pokedex.add_pokemon(leg)

pokedex.add_pokemon(mag)

mag.set_attributes('Agua')
leg.set_attributes('All')

print(leg)
print(pokedex)

pokedex.compare()

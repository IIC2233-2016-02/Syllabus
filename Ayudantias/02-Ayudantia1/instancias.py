class Dragon():
    def __init__(self):
        self.attack = 'Garra de Dragon'

class Fire():
    def __init__(self):
        self.attack = 'Lanzallamas!'

class Pokemon():
    def __init__(self):
        self.attack = 'Soy un pokemon!'

    def __repr__(self):
        return 'hola soy charmander'

class Charizard(Dragon, Fire, Pokemon):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Flareon(Pokemon, Fire):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


pokemon = Charizard()
print(pokemon)
print(type(pokemon) == Charizard)
print(type(pokemon) == Pokemon)
print(type(pokemon) == Fire)
print(pokemon.attack)
print(isinstance(Charizard, Pokemon))

# print(issubclass(pokemon, Charizard))
print(issubclass(Charizard, Pokemon))
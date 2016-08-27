class Dragon():
    def __init__(self):
        self.attack = 'Garra de Dragon'


class Fire():
    def __init__(self):
        self.attack = 'Lanzallamas!'


class Pokemon():
    def __init__(self):
        self.attack = 'Soy un pokemon!'


# Las tres clases anteriores tienen el atributo 'attack' que muestra algo distinto



class Charizard(Fire, Dragon, Pokemon):
    'Es importante el orden en que esta heredando'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


pokemon = Charizard()

# A pesar de estar heredando de Pokemon y Fire, type nos arroja False!
print(type(pokemon) == Charizard)
print(type(pokemon) == Pokemon)
print(type(pokemon) == Fire)
print('-' * 15)

# Pero con isinstance puedo saber si la instancia es de una clase que hereda de otra
print(isinstance(pokemon, Charizard))
print(isinstance(pokemon, Pokemon))
print('-' * 15)

# Cambia el orden en que hereda en la clase Charizard y cambiara el orden del mro y print de attack
print(Charizard.__mro__)  # En este orden buscara attack hasta encontrarlo
print(pokemon.attack)  # Muestra el resultado de Fire, ya que al encontrar attack deja de buscar en las otras clases


# Lo siguiente es un ejemplo
# print(issubclass(pokemon, Charizard))
print(issubclass(Charizard, Pokemon))
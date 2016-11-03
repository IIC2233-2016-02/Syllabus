import pickle
import json
import clases.py

def leer_jugadores(archivo):
    jugadores = {}
    with open(archivo, 'r') as file:
        _jugadores = json.load(file)
        for k, v in values.items():
            _player = Player(k, None)
            _player.update(**v)
            jugadores[k] = _player
    return jugadores

class CustomEncoder(json.JSONEncoder):
    pass


def main():
    #jugadores = leer_jugadores(archivo)
    pass


if __name__ == '__main__':
    main()

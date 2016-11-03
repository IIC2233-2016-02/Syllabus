class Team():
    def __init__(self, nombre, *jugadores):
        self.nombre = nombre
        self.jugadores = list(jugadores)
        self.fecha_modificacion = None

    def update_players(self, *jugadores):
        for jugador in jugadores:
            if type(jugador) == Player and not (jugador in self.jugadores):
                self.jugadores.append(jugador)
            else:
                raise Exception("Value is not type Player")

    def show_players(self):
        print(self)
        print(*self.jugadores, sep="\n")

    def __repr__(self):
        return "Equipo {0}".format(self.nombre)


class Player():
    def __init__(self, ide, nombre):
        self.id = ide
        self.nombre = nombre
        self.asistencias = None
        self.goles = None
        self.amarillas = None
        self.faltas = None
        self.rojas = None
        self.equipo = None

    def __repr__(self):
        return 'ID Jugador {0}'.format(self.id)

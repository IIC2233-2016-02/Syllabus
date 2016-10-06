#!/usr/bin/env python
#  -*- coding: utf-8
__author__ = 'joaquin'
from random import randint, uniform, choice


class Auto:
    num = 0

    def __init__(self, tiempo_inicial):
        self.tiempo_inicial = tiempo_inicial
        self.velocidad = randint(30, 40)
        self.recorrido = 0
        self.rendimiento = uniform(0.1, 0.07)  #l/km
        self.estanque = randint(40, 50)
        self.id = Auto.num
        Auto.num += 1

    def avanzar(self):
        self.recorrido += self.velocidad
        self.estanque -= self.rendimiento*self.velocidad

    def __repr__(self):
        return str(self.id)


class Ruta:
    names = ["Ruta 68", "Ruta 78", "Costanera Norte", "Kennedy", "Vespucio", "Ruta 5"]

    def __init__(self, largo, nombre, p_auto):
        self.nombre = nombre
        self.largo = largo
        self.probabilida_auto = p_auto
        self.cars = list()
        self.autos_en_pana = 0
        self.autos_terminaron = 0

    def add_new_car(self, tiempo):
        self.cars.append(Auto(tiempo))

    def remove_car(self, car):
        self.cars.remove(car)

    def __repr__(self):
        return self.nombre


class Simulacion2:

    def __init__(self, tiempo_maximo):
        self.tiempo_maximo = tiempo_maximo
        self.rutas = [Ruta(randint(350, 500), choice(Ruta.names), uniform(0.05, 0.08)) for _ in range(4)]

    def run(self):
        for t in range(self.tiempo_maximo):
            for ruta in self.rutas:
                for auto in ruta.cars:
                    auto.avanzar()
                    if auto.estanque <= 0:
                        print("[PANA EN {}]{}: Auto {} se quedó en pana en el km {}"
                              "".format(ruta, t, auto, auto.recorrido))
                        ruta.autos_en_pana += 1
                        ruta.remove_car(auto)
                    elif auto.recorrido >= ruta.largo:
                        print("[LLEGADA EN {}]{}: Auto {} llegó a su destino".format(ruta, t, auto))
                        ruta.remove_car(auto)
                        ruta.autos_terminaron += 1
                if ruta.probabilida_auto > uniform(0, 1):
                    ruta.add_new_car(t)
        print("Terminó la simulación")
        for ruta in self.rutas:
            print("En {} {} autos se quedaron en pana, y {} autos llegaron al final de la "
                  "ruta".format(ruta, ruta.autos_en_pana, ruta.autos_terminaron))

if __name__ == "__main__":
    simulacion = Simulacion2(5000)
    simulacion.run()

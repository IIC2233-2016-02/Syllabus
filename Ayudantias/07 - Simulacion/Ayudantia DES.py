#!/usr/bin/env python
#  -*- coding: utf-8
__author__ = 'joaquin'
from random import expovariate, randint, sample, uniform


class Auto:
    num = 0

    def __init__(self, tiempo_inicial, por_recorrer):
        self.tiempo_inicial = tiempo_inicial
        # Variables aleatorias
        self.rendimiento = uniform(0.1, 0.07)  # litros/kilometros
        self.estanque = randint(40, 50)  # litros
        self.velocidad = randint(30, 40)  # kilometros/hora
        self.llega = (self.estanque / self.rendimiento) / self.velocidad > por_recorrer / self.velocidad
        self.recorrido = por_recorrer if self.llega else (self.estanque / self.rendimiento) / self.velocidad
        # Identificacion de instancias
        self.id = Auto.num
        Auto.num += 1

    def __repr__(self):
        return str(self.id)

    @property
    def siguiente_evento(self):
        # Vemos que pasa primero: auto queda en pana o llega
        pana = (self.estanque / self.rendimiento) / self.velocidad
        llegada = self.recorrido / self.velocidad
        return min(pana, llegada)


class Ruta:
    nombres_rutas = ["Ruta 68", "Ruta 78", "Costanera Norte", "Kennedy", "Vespucio", "Ruta 5"]

    def __init__(self, largo, nombre, p_auto):
        self.nombre = nombre
        self.largo = largo
        # Variable aleatoria
        self.siguiente_auto = expovariate(p_auto)
        self.tasa_llegada = p_auto
        self.autos = list()
        self.autos_en_pana = 0
        self.autos_terminaron = 0

    @property
    def siguiente_evento(self):
        auto = self.siguiente_auto
        # Tomamos el auto que tiene el siguiente evento
        if len(self.autos) > 0:
            auto = min(self.autos, key=lambda c: c.siguiente_evento).siguiente_evento
            # Tomamos el siguiente evento en el auto para saber si queda en pana o llega
        return min(self.siguiente_auto, auto)

    def agregar_auto(self, tiempo):
        # Agregamos un nuevo auto
        self.autos.append(Auto(tiempo, self.largo))
        # Calculamos el tiempo en que llegara el siguiente
        self.siguiente_auto = tiempo + expovariate(self.tasa_llegada)

    def quitar_auto(self, auto):
        # Quitamos el auto de la lista
        self.autos.remove(auto)

    def __repr__(self):
        return self.nombre


class Simulacion2:

    def __init__(self, tiempo_maximo):
        self.tiempo_maximo = tiempo_maximo
        self.tiempo_actual = 0
        # Llenamos las rutas con valores aleatorios
        self.rutas = [Ruta(randint(350, 500), ruta, uniform(0.05, 0.1))
                      for ruta in sample(Ruta.nombres_rutas, 4)]

    @property
    def siguiente_evento(self):
        # Tomamos la ruta en la que ocurre el siguiente evento y luego el evento
        return min(self.rutas, key=lambda r: r.siguiente_evento).siguiente_evento

    def run(self):
        # MIENTRAS el tiempo de simulacion no termine
        while self.tiempo_maximo >= self.tiempo_actual:
            # AVANZAMOS el tiempo de simulacion al momento del evento
            self.tiempo_actual = self.siguiente_evento
            for ruta in self.rutas:
                # SIMULAMOS el evento que corresponda
                for auto in ruta.autos:                    
                    if auto.siguiente_evento == self.tiempo_actual and not auto.llega:
                        print("[PANA EN {}]{}: Auto {} se quedó en pana en el km {}"
                              "".format(ruta, self.tiempo_actual, auto, auto.recorrido))
                        ruta.autos_en_pana += 1
                        ruta.quitar_auto(auto)
                    elif auto.siguiente_evento == self.tiempo_actual and auto.llega:
                        print("[LLEGADA EN {}]{}: Auto {} llegó a su destino".format(
                            ruta, self.tiempo_actual, auto))
                        ruta.quitar_auto(auto)
                        ruta.autos_terminaron += 1
                if ruta.siguiente_auto == self.tiempo_actual:
                    ruta.agregar_auto(self.tiempo_actual)
        # Al terminar la simulacion imprimimos los resultados pedidos
        print("Terminó la simulación")
        for ruta in self.rutas:
            print("En {} {} autos se quedaron en pana, y {} autos llegaron al final de la "
                  "ruta".format(ruta, ruta.autos_en_pana, ruta.autos_terminaron))

if __name__ == "__main__":
    simulacion = Simulacion2(5000)
    simulacion.run()

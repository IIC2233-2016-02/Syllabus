import logging
import random
logging.basicConfig(ilename='AC09.log', format='%(asctime)s : %(levelname)s : %(message)s',
                    level=logging.INFO, filemode='w+')
random.seed(0)
logging.info()
ENTREGA_COMIDA = "Se ha entregado la comida de una mesa"
SENTARSE = "Un grupo ha obtenido una mesa"
PACIENCIA_COMIDA = "El grupo perdió la paciencia esperando la comida"
PACIENCIA_FILA = "El grupo perdió la paciencia esperando una mesa libre"
LLEGADA_CLIENTE = "Ha llegado un nuevo grupo al restaurant"
PAGAR = "Un grupo ha terminado de comer y ha ido a pagar"


def report_event(time, event):
    logging.info('SIMULATION TIME : {} : {}'.format(time, event))


from threading import Thread, Lock
from random import choice, randint
from time import sleep


# Este ejemplo es cuando se tiene que bloquear el acceso a un recurso que 
# pertenece a una instancia en particular. En este caso, el recurso es la lista 
# que contiene todas las piezas de una pizza.


class Pizza:

	def __init__(self, name):
		self.name = name
		self.__pieces = [ _ for _ in range(1, 9)]

		# Se crea un lock para sincronizar el acceso al recurso de la instancia
		self.__lock_pizza = Lock()

	def get_piece(self):
		if self.__pieces:
			# se usa el lock en el momento que se accede al recurso
			with self.__lock_pizza:
				piece = self.__pieces.pop()
			return piece
		return None


class Bastian(Thread):
	_id = 0

	def __init__(self, pizzas):
		super().__init__()
		self.__id = Bastian._id
		Bastian._id += 1
		self.__pizzas = pizzas

	def run(self):

		print('Bastian {} comienza a comer'.format(self.__id))
		
		while len(self.__pizzas)>0:

			pizza = choice(self.__pizzas)
			piece = pizza.get_piece()

			if piece:
				print('Bastian {} esta comiendo el pedazo {} de la '
                      'pizza {}'.format(self.__id, piece, pizza.name))
				# Se demora 1 a 3 segundos en comer la pizza #100%RealNoFake
				sleep(randint(1, 3)) 
			else:
				# Si no quedan pedazos se quita la pizza.
				self.__pizzas.remove(pizza)


		print ('Bastian {} se comio toda la pizza '
			   '(como siempre)'.format(self.__id))


if __name__ == '__main__':
	pizzas = [Pizza('Hawaiana'), Pizza('Pollo BBQ')]

	# comenzamos los threads:
	for _ in range(3):
		bati = Bastian(pizzas)
		bati.start()



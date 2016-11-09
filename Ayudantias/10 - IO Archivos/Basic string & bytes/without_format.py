from random import randint, random

names = ['Juan Cortes', 'Cristian Cortes', 'Anders Skog', 'Bastian Mavrakis', 'Matias Junemann']
binarios = [1010, 1, 1101, 11001, 11]
print('{0}|{1}|{2}'.format('Nombre', 'Nota', 'Numero'))
for alumno in names:
	nota = randint(0,6)*random() + 1
	print('{0}|{1}|{2}'.format(alumno, nota, binarios.pop()))
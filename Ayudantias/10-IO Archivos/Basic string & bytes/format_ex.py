from random import randint, random

names = ['Juan Cortes', 'Cristian Cortes', 'Anders Skog', 'Bastian Mavrakis', 'Matias Junemann']
binarios = [1010, 1, 1101, 11001, 11]
print('{0:20}|{1:5}|{2:.8}'.format('Nombre', 'Nota', 'Numero'))
for alumno in names:
	nota = randint(0,6)*random() + 1
	print('{0:20s}|{1:5.2f}|{2:0>8d}'.format(alumno, nota, binarios.pop()))
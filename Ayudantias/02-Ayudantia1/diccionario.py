ayudante = {'nombre': 'Anders', 'Major': 'Computacion', 'jerarquia': 'TPD'}

#Obtenemos llaves y valores 
print(ayudante.keys())
print(ayudante.values())

# Borraremos la llave jerarquia
del ayudante['jerarquia']
print(ayudante)

# Creamos la llave jerarquia nuevamente, con su correcto valor
ayudante['jerarquia'] = 'Jefe'
print(ayudante)

# Bastian no esta de acuerdo, modificamos el valor
ayudante['jerarquia'] = 'TPD'
print(ayudante)

#Creamos nueva llave
ayudante['minor'] = 'Industrial'
print(ayudante)

#iteramos sobre el diccionario
for llave in ayudante:
	print(ayudante[llave])

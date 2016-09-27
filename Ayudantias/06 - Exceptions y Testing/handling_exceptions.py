#  Ay. de Exceptions y Test


def get_first_course(estudiante, key):
    if estudiante.get(key) == None:  # No existe la llave!
        raise Exception('No es un estudiante')
    elif len(estudiante[key]) == 0:
        raise IndexError('No hay cursos aprobados')
    return estudiante[key][0]


alumno = {'num': 12345678, 'name': 'Juan', 'ramos_aprobados': [
    'Calculo', 'Programacion Avanzada', 'Electro']}
alumno2 = {'num': 11111111, 'name': 'Freddie', 'ramos_aprobados': [
    'Algebra', 'Programacion Avanzada', 'Discretas']}
novato = {'num': 87654321, 'name': 'Pedro', 'ramos_aprobados': []}
profesor = {'num': 5428769J, 'name': 'Diego',
            'cursos_dictados': ['Termo', 'Fluidos']}

# Ahora queremos ver como funcionara nuestra funcion
try:
    file = open('Cursos.txt', 'w')
    curso = ''
    # Probar cambiando el orden de novato y profesor
    for persona in [alumno, alumno2, novato, profesor]:
        curso += get_first_course(persona, 'ramos_aprobados') + ' '
    file.write(curso)
except IndexError:
    print('El alumno no ha pasado nada :(')
except Exception:
    print('Ingresaste un valor incorrecto')
else:
    print('No tuvo ningun error!!!')
finally:
    print(
        'Estos son los primeros ramos aprobados que recolectamos: {}'.format(curso))
    print('Cerramos el archivo')
    file.close()

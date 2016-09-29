import random
from functools import reduce
import string


def Verificador(rut):
    verificador = rut[-1]
    numero = rut[0:-2][::-1]
    suma = 0
    numeros = [2, 3, 4, 5, 6, 7]

    for i in range(len(numero)):
        suma += int(numero[i]) * numeros[i % 6]
    resto = suma % 11
    num = str(11 - resto)
    if 11 - resto == 10:
        num = 'k'
    elif 11 - resto == 11:
        num = "0"

    return num == verificador


def protect(function):
    def __protect(*args, **kw):
        if int(args[0].rut[:-2] + args[0].generar_codigo) % 97 == 1:
            return function(*args, **kw)
        raise Exception("Rut+codigo no compatibles!")
    return __protect


class PrograSU:


    def __init__(self, filename):
        self.subject = filename
        self.students = []
        self.questions = {}
        with open("{}.txt".format(filename),"r") as reader:
            for line in reader:
                list = line.split(",")
                self.questions[list[0]] = {"a":list[1], "b":list[2], "c": list[3], "answer": list[4].strip()}

    def register(self, obj):
        if type(obj) == Student:
            obj.answers[self.subject] = {}
            self.students.append(obj)
            self.students.sort(key=lambda x: x.final_score, reverse=True)
            return True
        return False

    def start_test(self):
        for student in self.students:
            self.take_test(student)

    def check_answer(self, number, answer):
        if self.questions[number] == answer:
            return True
        return False

    def take_test(self, student):

        ''' Aquí se simula a los alumnos realizando la prueba. Considera
        que el alumno tiene 2/3 de probabilidad de responder correctamente,
        y sino, se elige una letra aleatoria en el abecedario.'''

        print("{} se encuentra realizando el test".format(student.name))
        student.answers[self.subject] = {}
        for question in self.questions:
            p = random.choice([1, 1, 0])
            if p == 1:  # Respuesta correcta
                answer = self.questions[question]["answer"]

            else:
                answer = random.choice(string.ascii_letters)

            if self.questions[answer] == self.questions["answer"]:
                student.answers[self.subject][question] = True
            else:
                student.answers[self.subject][question] = False
        print("{} ha terminado el test".format(student.name))

    def see_student(self, number):
        print("El alumno con lugar numero {0} en la prueba de {1} es {2}".format(number, self.subject,
                                                                                 self.students[number].name))
        return self.students[number]


class Student:


    def __init__(self, name, age, rut, school):
        self.name = name
        self.age = age
        self.school = school
        self.rut = rut
        self.scores = {}
        self.answers = {}
        self.final_score = -1

    @property
    def generar_codigo(self):
        return (98 - self.rut[:-2] * 100 % 97) % 97

    def get_best_score(self):
        return max(self.scores, key=lambda x: self.scores[x])

    @protect
    def get_test_results(self, subject):
        correct = len(
            list(filter(lambda answer: self.answers[subject][answer], self.answers[subject])))

        self.scores[subject] = 850 * (correct - ((len(self.answers[subject]) - correct) / 4)) / len(
            self.answers[subject])

        return "El resultado de {0} fue de {1} puntos".format(subject, self.scores[subject])

    @protect
    def get_final_score(self):
        self.final_score = sum(
            reduce(lambda score_1, score_2: self.scores["Lenguaje"] + self.scores["Matematicas"], self.scores)) / len(
            self.scores)
        return "El resultado final de {0} fue de {1} puntos".format(self.name, self.final_score)


if __name__ == "__main__":
    # Creo las pruebas online con las preguntas
    mat = PrograSU("Matematicas")
    leng = PrograSU("Lenguaje")

    # Inscribo los alumnos
    # Freddie ingresa mal el rut
    freddie_1 = Student("Freddie", 20, 19243656 - 7, "ke ez ezo")
    freddie_2 = Student("Freddie", 20, "19243656-7", "ke ez ezo")
    mat.register(freddie_2)
    leng.register(freddie_2)

    anders = Student("Anders", 20, "19243656-7", "grange")
    mat.register(anders)

    juan = Student("Juan", 20, "19243656-7", "del sur")
    mat.register(juan)

    # Los alumnos inscritos rinden las pruebas
    mat.start_test()
    leng.start_test()

    # Obtengo un alumno que no existe
    student_1 = mat.see_student(3)  # solo hay tres
    # Obtengo uno que si existe
    student_2 = mat.see_student(1)  # se que hay alguno

    print(student_2.get_test_results("Matematicas"))
    # Intento obtener resultados de materia que no existe
    print(student_2.get_test_results("Historia"))

    # Incsribo el lenguaje a otro alumno que llego tarde y no alcanza a dar
    # ninguna prueba
    cote = Student("Cote", 22, "18641025-4", "everest")
    leng.register(cote)
    
    # Intenta ver resultados que no existen
    print(cote.get_test_results("Lenguaje"))
    print(cote.get_final_score())

    print(juan.get_best_score())

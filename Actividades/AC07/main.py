import random

name_list = ['Alfonso', 'Benito', 'Alfredo', 'Geronimo', 'Peter', 'Jack',
             'Simon', 'Jaime', 'Bego', 'Francisca', 'Maida', 'Clara', 'Rocio',
             'Sofia', 'Belen', 'Fausto', 'Juan', 'Miguel', 'Mariana',
             'Fernanda', 'Constanza', 'Valentina', 'Tomas']

lastname_list = ['Fernández', 'Rodríguez', 'González', 'García', 'López',
                 'Martínez', 'Pérez', 'Álvarez', 'Gómez', 'Sánchez',
                 'Díaz', 'Vásquez', 'Castro', 'Romero', 'Suárez']


# Solo modificar para agregar metaclass=*
class Boss():
    def __init__(self, organization, *args, **kwargs):
        self.organization = organization

    def __repr__(self):
        return 'Boss: {0.name} {0.last_name}'.format(self)


class Worker():
    def __init__(self, organization, *args, **kwargs):
        self.organization = organization

    def __repr__(self):
        return 'Worker: {0.name} {0.last_name}'.format(self)


class Organization():

    def __init__(self, name):
        self.name = name
        self.boss = None
        self.members = list()

    def __repr__(self):
        return 'Organizacion: {}'.format(self.name)

    def pick_one_worker(self):
        return random.choice(self.members)


if __name__ == '__main__':
    salo = Organization('Salo')
    print(salo)
    salo()
    print()
    sola = Organization('Sola')
    print(sola)
    sola()

    z = Organization('Salo')
    print("Nombres utilizados {}".format(Organization.used_names))
    print()

    jefe_salo = Boss(salo)
    jefe_sola = Worker(sola)
    jefe_sola = Boss(sola)
    print()

    for i in range(3):
        w = Worker(salo)
        jefe_salo.add_member(w)
        w.to_work()
    salo.pick_one_worker().to_work()
    jefe_salo.order()
    print()
    for i in range(2):
        jefe_sola.add_member(Worker(sola))
    sola.pick_one_worker().to_work()
    jefe_sola.order()

    new_jefe_salo = Boss(salo)

    print('--'*50)
    salo()
    salo.see_members()
    print('--'*50)
    sola()
    sola.see_members()
    print('--'*50)

class Metaclass(type):
    message = 'mcs/cls: {}\nname: {}\nbases: {}\nattrs: {}'

    def __new__(mcs, name, bases, attrs):
        print('# <__new__> ¡Argumentos iniciales!')
        print(Metaclass.message.format(mcs, name, bases, attrs))

        # <Modificando>
        name = 'B'
        bases = (object, )
        attrs = {'foo': lambda: print('Lorem Ipsum')}
        # </Modificando>
        
        print('# <__new__> ¡Argumentos modificados!')
        print(Metaclass.message.format(mcs, name, bases, attrs))
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print('# <__init__> ¡Argumentos iniciales!')
        print(Metaclass.message.format(cls, name, bases, attrs))
        return super().__init__(name, bases, attrs)


class A(metaclass=Metaclass):
    pass


if __name__ == '__main__':
    print(A.__name__)
    A.foo()


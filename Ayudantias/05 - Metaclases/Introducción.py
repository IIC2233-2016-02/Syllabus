class A:
    pass

if __name__ == '__main__':
    # ¡Las clases también son objetos!
    reference = A
    instance = reference()
    print(instance)

    message = 'Type de {0} es {1}'

    # Si las clases son objetos... ¿De donde provienen?
    print(message.format('A', type(A)))

    # Todas las clases tienen un padre en común.
    print(message.format('int', type(int)))
    print(message.format('str', type(str)))
    print(message.format('type', type(type)))

    # Podemos instanciar clases mediante type.
    message = '¡Soy una instancia de la clase {0}!'
    B = type('B', (A,), {
        'method': lambda s: print(message.format(s.__class__.__name__))
    })

    # Creando una instancia de la clase instanciada a partir de la metaclase.
    b = B()
    b.method()


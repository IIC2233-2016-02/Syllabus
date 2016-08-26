import sys

def test(a, b, *argv):
    print(a)
    print(b)
    print(argv)
    for arg in argv:
        print("siguiente argumento de *argv : {}".format(arg))

test('hola','como','va','todo')
test('hola','como', 'estas')
test('hola','hola')
#test('hola')

print(sys.argv)
test(*sys.argv)



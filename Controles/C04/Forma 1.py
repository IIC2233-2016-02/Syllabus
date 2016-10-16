class Aux:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return '{} - {}'.format(self.a, self.b)


def bar(l):
    l.b += 2
    return l

foo = [Aux(a, b) for a, b in zip(range(3), range(3))]

print(foo)

r = list(map(bar, filter(lambda x: x.a % 2 == 0, foo)))

print(r)

print(foo)


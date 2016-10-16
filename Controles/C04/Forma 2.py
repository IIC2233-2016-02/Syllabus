from functools import reduce


p = [['0001', 'A', 2, 1000],
     ['0002', 'B', 3, 3000],
     ['0003', 'C', 20, 200]]

o = (3, 0.9)

t = list(map(lambda x: (x[0], x[2]) if x[1] != o[0] else (x[0], x[2] * o[1]), map(lambda x: (x[0], x[2], x[2] * x[3]), p)))
print(t)

m = reduce(lambda a, b: a if (a > b) else b, map(lambda x: x[1], t))
print(m)


#!/usr/bin/python

def walk(w, p):
    if len(w) == 0:
        return []
    c = w[0]
    d = (1j)**"RULD".index(c[0])
    b = int(c[1:])
    r=list(map(lambda i: p+(i+1)*d, range(b)))
    return r + walk(w[1:], r[-1])

f = open("day3_input")
w1 = f.readline().split(",")
w2 = f.readline().split(",")
walk2 = set(walk(w2, 0))
res = map(lambda x: abs(x.real) + abs(x.imag), filter(lambda x: x in walk2, walk(w1, 0)))
print(sorted(res)[0])

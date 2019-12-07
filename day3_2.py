#!/usr/bin/python

def walk(w, p, steps):
    if len(w) == 0:
        return []
    c = w[0]
    dir = (0+1j)**"RULD".index(c[0])
    count = int(c[1:])
    res = list(map(lambda i: (p+(i+1)*dir, steps+i+1), range(count)))
    return res + walk(w[1:], res[-1][0], steps+count)

f = open("day3_input")
w1 = f.readline().split(",")
w2 = f.readline().split(",")
walk2 = set(walk(w2, 0, 0))
w2_pos = set(map(lambda x: x[0], walk2))
res = map(lambda d: d[1]+list(sorted(filter(lambda c: c[0]==d[0], walk2), key=lambda b: b[1]))[0][1], filter(lambda a: a[0] in w2_pos, walk(w1, 0, 0)))
print(sorted(res)[0])

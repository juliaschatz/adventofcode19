#!/usr/bin/python

import itertools

def calculate(signal, phase):
    inp = phase
    f = open("day7_input")
    computer = list(map(int, f.readline().split(",")))
    f.close()
    i = 0
    while computer[i]%100 != 99:
        c = computer[i] % 100
        p = list(map(lambda j: (computer[i] // 10**j) % 10 == 1, range(2, 5)))
        def access(n):
            return computer[i+n if p[n-1] else computer[i+n]]
        def store(n, v):
            computer[computer[i+n]] = v
        if c == 1: #sum
            a = access(1)
            b = access(2)
            store(3,a+b)
            i+=4
        elif c == 2: #mul
            a = access(1)
            b = access(2)
            store(3, a*b)
            i+=4
        elif c == 3: #input
            store(1, inp)
            inp = signal
            i+=2
        elif c == 4: # print
            return(access(1))
            i+=2
        elif c == 5: # jump if true
            if access(1) != 0:
                i = access(2)
            else:
                i+=3
        elif c == 6: # jump if false
            if access(1) == 0:
                i = access(2)
            else:
                i+=3
        elif c == 7: # less than
            store(3, access(1) < access(2))
            i+=4
        elif c == 8: # equals
            store(3, access(1) == access(2))
            i+=4

max_ = 0
for phases in itertools.permutations(range(5)):
    outp = 0
    for i in range(5):
        outp = calculate(outp, phases[i])
    if outp > max_:
        max_ = outp
print(max_)
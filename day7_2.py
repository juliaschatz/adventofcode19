#!/usr/bin/python

import itertools

def calculate(phase):
    inp = phase
    yield_inp = False
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
            if yield_inp:
                inp = yield
            yield_inp = True
            store(1, inp)
            i+=2
        elif c == 4: # print
            sig = access(1)
            yield sig
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
            store(3, 1 if access(1) < access(2) else 0)
            i+=4
        elif c == 8: # equals
            store(3, 1 if access(1) == access(2) else 0)
            i+=4
    while True:
        _ = yield
        yield None

max_ = 0
for phases in itertools.permutations(range(5, 10)):
    gens = list(map(lambda i: calculate(phases[i]), range(5)))
    next(gens[0])
    signal = gens[0].send(0)
    run = True
    while run:
        for i in range(5):
            j = (i+1)%5
            next(gens[j]) # run next amplifier until input yield
            signal_ = gens[j].send(signal) # get the output of next amplifier
            if signal_ is None: # break immediately if output is None, this means we looped around back to the beginning and we are finished
                run = False
                break
            signal = signal_
    if signal > max_:
        max_ = signal
print(max_)
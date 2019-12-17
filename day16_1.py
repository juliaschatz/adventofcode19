#!/usr/bin/python

import math

with open("day16_input") as f:
    p = list(f.readline()[:-1])
    base = [0, 1, 0, -1]
    def get_pattern(pc, inp_len):
        pattern = []
        for item in base:
            pattern += [item]*pc
        pattern *= int(math.ceil(inp_len / len(pattern)))+1
        return pattern[1:]
    
    def fft(inp):
        outp = []
        for i in range(1, len(inp)+1):
            pattern = get_pattern(i, len(inp))
            outp.append(abs(sum(map(lambda j: pattern[j] * inp[j], range(len(inp))))) % 10)
        return outp

    inp = list(map(int, p))
    for i in range(100):
        inp = fft(inp)
    print((''.join(map(str, inp)))[:8])


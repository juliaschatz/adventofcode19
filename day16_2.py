#!/usr/bin/python

import math

with open("day16_input") as f:
    p = list(f.readline()[:-1])
    def fast_fft(inp, ofs):
        outp = [0]*ofs
        outp.append(sum(inp[ofs:]))
        for i in range(ofs, len(inp)):
            outp.append(outp[-1] - inp[i])
            #print(f"Position {i} result: {outp[-1]}")
        return list(map(lambda x: abs(x)%10, outp))
    inp = list(map(int, p))*10000
    ilen = len(inp)
    ofs = int(''.join(map(str,inp[:7])))
    print(f"length: {ilen} offset: {ofs} remaining length: {ilen - ofs}")
    for i in range(100):
        print(i)
        inp = fast_fft(inp, ofs)
    print((''.join(map(str, inp)))[ofs:ofs+8])

#!/usr/bin/python

import time

visualize = True

if __name__ == '__main__':
    with open("day11_input") as f:
        pos = 0
        dir = 0+1j
        squares = {}

        paint = True
        did_thing = True

        computer = list(map(int, f.readline().split(",")))
        computer += [0]*1024
        i = 0
        relbase = 0
        while computer[i]%100 != 99:
            c = computer[i] % 100
            p = list(map(lambda j: (computer[i] // 10**j) % 10, range(2, 5)))
            def param(n):
                if p[n-1] == 1:
                    return i+n
                if p[n-1] == 2:
                    return relbase+computer[i+n]
                else:
                    return computer[i+n]
            def access(n):
                return computer[param(n)]
            def store(n, v):
                computer[param(n)] = v
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
                store(1, squares[pos] if pos in squares.keys() else 0)
                paint = True
                i+=2
            elif c == 4: # print
                val = access(1)
                did_thing = True
                if paint:
                    paint = False
                    squares[pos] = val
                else:
                    dir *= (0+1j) if val == 0 else (0-1j)
                    pos += dir
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
            elif c == 9: # update relative base
                relbase += access(1)
                i+=2
            if visualize and did_thing and len(squares) > 0:
                wmin = int(min(squares.keys(), key=lambda z: z.real).real)
                wmax = int(max(squares.keys(), key=lambda z: z.real).real)
                hmin = int(min(squares.keys(), key=lambda z: z.imag).imag)
                hmax = int(max(squares.keys(), key=lambda z: z.imag).imag)
                for b in reversed(range(hmin, hmax+1)):
                    for a in range(wmin, wmax+1):
                        p = a + (1j)*b
                        if p == pos:
                            if dir == 1:
                                k = ">"
                            elif dir == 1j:
                                k = "^"
                            elif dir == -1:
                                k = "<"
                            elif dir == -1j:
                                k = "v"
                            print(k, end="")
                        else:
                            if p in squares:
                                val = squares[p]
                            else:
                                val = 0
                            print("█" if val==1 else ".", end="")
                    print()
                did_thing = False
                print()
                time.sleep(0.001)
        print(len(squares))
        
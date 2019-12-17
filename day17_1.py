#!/usr/bin/python

import time
import copy
import random
    
visualize = True

if __name__ == '__main__':
    with open("day17_input") as f:
        computer = list(map(int, f.readline().split(",")))
        computer += [0]*2048
        i = 0
        relbase = 0
        
        screen = ""

        did_thing = False
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
                store(1, 0)
                i+=2
            elif c == 4: # print
                val = access(1)
                screen += chr(val)
                did_thing = True
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
        if visualize:
            print(screen)
        screen = screen.split("\n")
        screen = list(map(list, screen))
        checks = 0
        for i in range(len(screen)):
            for j in range(len(screen[i])):
                try:
                    if screen[i][j] == "#" and screen[i][j+1] == "#" and screen[i][j-1] == "#" and screen[i+1][j] == "#" and screen[i-1][j] == "#":
                        checks += i*j
                        screen[i][j] = "O"
                except IndexError:
                    continue
        for k in screen:
            print(''.join(k))
        print(checks)
        
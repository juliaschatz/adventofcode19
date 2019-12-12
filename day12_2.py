#!/usr/bin/python

import copy, math

def sign(x):
    return 0 if x == 0 else x//abs(x)

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

with open("day12_input") as f:
    moons = []
    vels = []
    for l in f.readlines():
        l = l[1:-2].split(", ")
        moon = []
        for i in range(3):
            moon += [int(l[i][2:])]
        moons.append(moon)
        vels.append([0, 0, 0])

    res = [0]*3
    base = [0]*3
    axstates = [set()]*3
    i = 0
    while True:
        i+=1
        for ax in range(3):
            if res[ax] == 0:
                chek = hash(tuple([m[ax] for m in moons] + [v[ax] for v in vels]))
                axstates[ax].update((chek,))
        # Acceleration
        for j, moon0 in enumerate(moons):
            for k, moon1 in enumerate(moons[:j]):
                for ax in range(3):
                    if res[ax] == 0:
                        vel = sign(moon1[ax] - moon0[ax])
                        vels[j][ax] += vel
                        vels[k][ax] -= vel
        
        # Position
        for j, moon0 in enumerate(moons):
            for ax in range(3):
                if res[ax] == 0:
                    moon0[ax] += vels[j][ax]
        
        for ax in range(3):
            chek = hash(tuple([m[ax] for m in moons] + [v[ax] for v in vels]))
            if res[ax] == 0 and chek in axstates[ax]:
                res[ax] = i

        if 0 not in res:
            break
    result = int(lcm(res[0], lcm(res[1], res[2])))
    
    print(result)
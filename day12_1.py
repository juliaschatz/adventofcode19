#!/usr/bin/python

def sign(x):
    return 0 if x == 0 else x//abs(x)

def energy(tup):
    return sum(map(abs, tup))

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
    
    for i in range(1000):
        # Acceleration
        for j, moon0 in enumerate(moons):
            for k, moon1 in enumerate(moons[:j]):
                for ax in range(3):
                    vel = sign(moon1[ax] - moon0[ax])
                    vels[j][ax] += vel
                    vels[k][ax] -= vel
        
        # Position
        for j, moon0 in enumerate(moons):
            for ax in range(3):
                moon0[ax] += vels[j][ax]
    
    print(sum(map(lambda i: energy(moons[i]) * energy(vels[i]), range(len(moons)))))
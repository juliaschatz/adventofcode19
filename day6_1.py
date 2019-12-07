#!/usr/bin/python

with open("day6_input") as f:
    orbits = {}
    for l in f.readlines():
        o = l.replace("\n","").split(")")
        orbits[o[1]] = o[0]
    def count(p):
        if orbits[p] == "COM":
            return 1
        return 1 + count(orbits[p])
    print(sum(map(count, orbits.keys())))
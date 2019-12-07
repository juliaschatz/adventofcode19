#!/usr/bin/python

with open("day6_input") as f:
    orbits = {}
    for l in f.readlines():
        o = l.replace("\n","").split(")")
        orbits[o[1]] = o[0]
    def order(p):
        if p == "COM":
            return ["COM"]
        return [p] + order(orbits[p])
    me = order("YOU")
    san = order("SAN")
    for i in range(len(me)):
        if me[i] in san:
            print(san.index(me[i]) + i - 2)
            break
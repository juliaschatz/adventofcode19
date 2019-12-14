#!/usr/bin/python

import math

with open("day14_input") as f:
    reactions = {}
    for line in f.readlines():
        reac = line.split(" => ")
        components = reac[0].split(", ")
        result = reac[1].split(" ")
        result_el = result[1][:-1]
        reactions[result_el] = {"_": int(result[0])}
        for c in components:
            c_ = c.split(" ")
            reactions[result_el][c_[1]] = int(c_[0])
    print(reactions)
    amounts = {}
    ore_count = 0
    for item in reactions:
        amounts[item] = 0
    amounts["ORE"] = 0
    def make(base):
        global ore_count
        if base == "ORE":
            ore_count += 1
            amounts["ORE"] += 1
            return
        r = reactions[base]
        amt_made = r["_"]
        for item in r:
            if item == "_":
                continue
            needed = r[item]
            while amounts[item] < needed:
                make(item)
            amounts[item] -= needed
        amounts[base] += amt_made
            
    make("FUEL")
    print(ore_count)

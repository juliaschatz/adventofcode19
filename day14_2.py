#!/usr/bin/python

import math
from itertools import product
import copy

def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

def lcm_(iitems):
    if len(iitems) == 2:
        return lcm(iitems[0], iitems[1])
    return lcm(iitems[0], lcm_(iitems[1:]))

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
    
    def calculate(amount_):
        amounts = {}
        ore_count = 0
        for item in reactions:
            amounts[item] = 0
        amounts["ORE"] = 0
        def make(base, amount):
            ore_ = 0
            r = reactions[base]
            amt_made = r["_"]
            t = math.ceil(amount / amt_made)
            for item in r:
                if item == "_":
                    continue
                needed = r[item]*t
                if item == "ORE":
                    ore_ += needed - amounts[item]
                    amounts[item] = needed
                else:
                    ore_ += make(item, needed - amounts[item])
                amounts[item] -= needed
            amounts[base] += amt_made*t
            return ore_
        
        return make("FUEL", amount_)

    target = 1000000000000
    cost0 = calculate(1)
    test = target // cost0

    a = calculate(test)
    b = calculate(test+1)
    d = 10000000
    last = a - target
    while not (a < target and b > target):
        if a > target:
            test -= d
            if last < 0:
                d = max(d // 10, 1)
        if a < target:
            test += d
            if last > 0:
                d = max(d // 10, 1)
        last = a - target
        a = calculate(test)
        b = calculate(test+1)
        print(test)
    print(test)

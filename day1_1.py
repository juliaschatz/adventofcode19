#!/usr/bin/python

def calc_fuel(line):
    num = int(line)
    return num // 3 - 2

if __name__ == '__main__':
    with open("day1_1_input", 'r') as f:
        print(sum(map(calc_fuel, f.readlines())))
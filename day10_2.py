#!/usr/bin/python

import math, time

def sign(x):
    return 0 if x == 0 else x/abs(x)

def printmap(lines):
    for l in lines:
        print(''.join(l),end="")
    print()

with open("day10_input") as f:
    asteroids = []
    def visible(pos):
        a_ = []
        for asteroid in asteroids:
            if asteroid == pos:
                continue
            dx = asteroid[0] - pos[0]
            dy = asteroid[1] - pos[1]
            vert = dx == 0
            can_see = True
            if vert:
                for i in range(1, abs(dy)):
                    realx = pos[0]
                    realy = pos[1] + sign(dy) * i
                    if (realx, realy) in asteroids:
                        can_see = False
                        break
            else:
                slope = dy/abs(dx)
                for i in range(1, abs(dx)):
                    y = slope*i 
                    if abs(y - round(y)) < 0.01:
                        realx = int(pos[0] + sign(dx) * i)
                        realy = int(pos[1] + round(y))
                        if (realx, realy) in asteroids:
                            can_see = False
                            break
            if can_see:
                a_ += [asteroid]
        return a_
    def vaporize(pos, dy, dx, visible):
        vert = abs(dx) < 0.0001
        can_see = True
        if vert:
            for i in range(1, abs(int(dy))):
                realx = pos[0]
                realy = pos[1] + int(sign(dy) * i)
                if (realx, realy) in visible:
                    return (realx, realy)
        else:
            slope = dy/abs(dx)
            for i in range(1, abs(int(dx))):
                y = slope*i 
                if abs(y - round(y)) < 0.01:
                    realx = int(pos[0] + sign(dx) * i)
                    realy = int(pos[1] + round(y))
                    if (realx, realy) in visible:
                        return (realx, realy)
    lines = list(map(list, f.readlines()))
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#": asteroids+=[(j,i)]
    p=(31, 20)
    lines[p[1]][p[0]] = "@"
    count = 0
    theta = 0
    last = None
    delta = 3600000
    while count < 200:
        visible_ = visible(p)
        for item in visible_:
            lines[item[1]][item[0]] = "+"
        printmap(lines)
        print(len(visible_))
        removed = []
        for i in range(delta):
            last = min(visible_, key=lambda a: -math.atan2(a[0]-p[0], a[1]-p[1]))
            if last is not None:
                for item in removed:
                    lines[item[1]][item[0]] = "."
                asteroids.remove(last)
                visible_.remove(last)
                removed += [last]
                lines[last[1]][last[0]] = "!"
                print(f"{count+1}: {last}")
                printmap(lines)
                time.sleep(0.1)
                print()
                count += 1
                if count == 200:
                    break
                    
    print(last[0]*100 + last[1])
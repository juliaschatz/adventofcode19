#!/usr/bin/python

def sign(x):
    return 0 if x == 0 else x/abs(x)

with open("day10_input") as f:
    asteroids = []
    def count_visible(pos):
        count = 0
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
                count += 1
        return count
    for i, line in enumerate(f.readlines()):
        for j, char in enumerate(line):
            if char == "#": asteroids+=[(j,i)]
    p=max(asteroids, key=count_visible)
    print(f"{p}, {count_visible(p)}")
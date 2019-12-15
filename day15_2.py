#!/usr/bin/python

import time
import copy
import random

visualize = True
wall = "█"
air = "."
oxy = "$"

renders = []

plist = [1j, -1j, -1, 1]
def adj(mapp, pt):
    for d in plist:
        if pt+d not in mapp or mapp[pt+d] in (air, oxy):
            yield pt+d

def adj_passable(mapp, pt):
    for d in plist:
        if pt+d in mapp and mapp[pt+d] in (air, oxy):
            yield pt+d

def get_d(move_cmd):
    if move_cmd == 1:
        d = 1j
    elif move_cmd == 2:
        d = -1j
    elif move_cmd == 3:
        d = -1
    else:
        d = 1
    return d

def shortest_path(mapp, source, goal):
    global renders
    boundary = [source]
    visited = []
    distances = {source: 0}
    distance_ = lambda x: 1000 if x not in distances else distances[x]
    current = source
    while True:
        neighbors = list(adj(mapp, current))
        for item in neighbors:
            if item not in boundary and item not in visited:
                boundary.append(item)
            if item in distances:
                distances[item] = min(distances[item], distances[current] + 1)
            else:
                distances[item] = distances[current] + 1
        boundary.remove(current)
        visited.append(current)
        if current == goal:
            path = []
            item = goal
            while item != source:
                path.append(item)
                renders = path
                candidates = [x for x in adj(mapp, item) if x not in path]
                if len(candidates) == 0:
                    return None
                item = min(candidates, key=distance_)
                if item == None:
                    return None
            return path
        if len(boundary) == 0:
            return None # Couldn't find path
        current = min(boundary, key=distance_)

def find_unpassed(mapp, source):
    visited = []
    visited += [source]
    queue = list(adj(mapp, source))
    while len(list(filter(lambda x: x not in mapp, visited))) == 0:
        try:
            item = queue.pop()
        except:
            return None
        news = [x for x in list(adj(mapp, item)) if x not in visited]
        visited += news
        queue += news
    target = list(filter(lambda x: x not in mapp, visited))[0]
    return target

def draw_map(mapp, renders):
    wmin = int(min(mapp.keys(), key=lambda z: z.real).real)
    wmax = int(max(mapp.keys(), key=lambda z: z.real).real)
    hmin = int(min(mapp.keys(), key=lambda z: z.imag).imag)
    hmax = int(max(mapp.keys(), key=lambda z: z.imag).imag)
    for b in reversed(range(hmin, hmax+1)):
        for a in range(wmin, wmax+1):
            p = a + (1j)*b
            if p in renders:
                val = "@"
            elif p == pos:
                val = "D"
            elif p in mapp:
                val = mapp[p]
            else:
                val = " "
            print(val, end="")
        print()
    print()

def calc_fill(mapp, pt):
    minutes = 0
    ox = [pt]
    boundary = list(adj(mapp, pt))
    if visualize:
        draw_map(mapp, ox)
        time.sleep(1)
    while len(boundary) > 0:
        l = copy.copy(boundary)
        for point in l:
            ox.append(point)
            boundary_ = list(adj(mapp, point))
            boundary += [x for x in boundary_ if x not in ox and x not in boundary]
            boundary.remove(point)
        if visualize:
            draw_map(mapp, ox)
            time.sleep(0.01)
        minutes += 1
    print(minutes)

if __name__ == '__main__':
    with open("day15_input") as f:
        computer = list(map(int, f.readline().split(",")))
        computer += [0]*1024
        i = 0
        relbase = 0
        pos = 0
        last_pos = 0
        move_dir = 0
        status = -1
        mapp = {0: air}

        end_pt = None
        
        active_path = None
        path_z = -1

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
                # Decide a movement command
                for j,d in enumerate(plist):
                    if pos+d not in mapp:
                        move_cmd = j+1
                        break
                else:
                    if active_path is not None:
                        if path_z < 0:
                            active_path = None
                        else:
                            move_cmd = plist.index(active_path[path_z] - pos) + 1
                            path_z -= 1
                            if path_z == 0:
                                active_path = None
                    else:
                        for j,d in enumerate(plist):
                            if mapp[pos+d] == air and pos+d != last_pos:
                                move_cmd = j+1
                                break
                        else:
                            target = find_unpassed(mapp, pos)
                            if target is not None:
                                path = shortest_path(mapp, pos, target)
                                if path is not None:
                                    move_cmd = plist.index(path[-1] - pos) + 1
                                    active_path = path
                                    path_z = len(path)-2
                                    did_thing = True
                                else:
                                    print("Couldn't find path")
                                    move_cmd = move_cmd if status != 0 else random.choice(range(1, 5))
                            else:
                                calc_fill(mapp, end_pt)
                                break
                store(1, move_cmd)
                i+=2
            elif c == 4: # print
                val = access(1)
                d = get_d(move_cmd)
                status = val
                if val == 0:
                    # Hit wall
                    mapp[pos + d] = wall
                    did_thing = True
                elif val == 1:
                    last_pos = pos
                    pos += d
                    mapp[pos] = air
                elif val == 2:
                    last_pos = pos
                    pos += d
                    mapp[pos] = oxy
                    end_pt = pos
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
            
        
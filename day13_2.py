#!/usr/bin/python

import time

visualize = True
size = 40

if __name__ == '__main__':
    with open("day13_input") as f:
        computer = list(map(int, f.readline().split(",")))
        computer += [0]*1024
        i = 0
        relbase = 0
        computer[0] = 2
        draw = []
        screen = [" "]*int(size**2)

        js_val = 0
        score = 0
        drawn_ball = False
        ball_x = 0
        paddle_x = 0


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
                store(1, js_val)
                i+=2
            elif c == 4: # print
                val = access(1)
                draw += [val]
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
            if len(draw) == 3:
                x = draw[0]
                y = draw[1]
                icon = draw[2]
                draw = []
                if x == -1 and y == 0:
                    score = icon
                else:
                    screen[y*size + x] = " █#-o"[icon]
                    drawn_ball = icon == 4
                    if icon == 4:
                        ball_x = x
                    if icon == 3:
                        paddle_x = x
                if ball_x < paddle_x:
                    js_val = -1
                elif ball_x > paddle_x:
                    js_val = 1
                else:
                    js_val = 0
                # Render screen
                print("\n"*100)
                print(f"{score}\n")
                for j in range(size):
                    for k in range(size):
                        print(screen[j*size+k], end="")
                    print()
                time.sleep(0.01 if drawn_ball else 0)
        
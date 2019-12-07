#!/usr/bin/python

if __name__ == '__main__':
    target = 19690720
    with open("day2_1_input") as f:
        fresh = list(map(int, f.readline().split(",")))
        computer = fresh[:]
        for noun in range(100):
            for verb in range(100):
                computer[1] = noun
                computer[2] = verb
                for i in range(0, len(computer), 4):
                    if computer[i] == 1:
                        a = computer[computer[i+1]]
                        b = computer[computer[i+2]]
                        computer[computer[i+3]] = a+b
                    elif computer[i] == 2:
                        a = computer[computer[i+1]]
                        b = computer[computer[i+2]]
                        computer[computer[i+3]] = a*b
                    elif computer[i] == 99:
                        break
                if computer[0] == target:
                    print(100 * noun + verb)
                    break
                computer = fresh[:]
            
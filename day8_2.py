#!/usr/bin/python


sz = 25*6
with open("day8_input") as f:
    st = f.readline().replace("\n", "")
    pic = ["2"]*sz
    for i in range(len(st)//sz):
        ly = st[i*sz:(i+1)*sz]
        for j in range(len(ly)):
            if pic[j] == "2":
                pic[j] = ly[j]
    pic = list(map(lambda x: "-█ "[int(x)], pic))
    for i in range(6):
        print(''.join(pic[i*25:(i+1)*25]))
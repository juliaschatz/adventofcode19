#!/usr/bin/python


sz = 25*6
with open("day8_input") as f:
    st = f.readline().replace("\n", "")
    minly = ""
    min_ = 10000
    for i in range(len(st)//sz):
        ly = st[i*sz:(i+1)*sz]
        if ly.count("0") < min_:
            min_ = ly.count("0")
            minly = ly
    print(minly.count("1") * minly.count("2"))
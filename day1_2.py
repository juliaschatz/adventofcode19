#!/usr/bin/python

def g(n):
    k=int(n)//3-2
    return 0 if k<0 else k+g(k)
print(sum(map(g,open("i").readlines())))
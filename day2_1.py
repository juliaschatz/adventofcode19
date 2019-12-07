#!/usr/bin/python

def g(i):
    p=c[i]
    if p==99:return
    a=c[c[i+1]]
    b=c[c[i+2]]
    c[c[i+3]]=a+b if p==1 else a*b
    g(i+4)
c=list(map(int,open("i").readline().split(",")))
c[1:3]=[12,2]
g(0)
print(c[0])
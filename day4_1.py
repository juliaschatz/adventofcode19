#!/usr/bin/python

def f(i):
    s=str(i)
    return ''.join(sorted(s))==s and any(map(lambda j: s[j]==s[j+1], range(len(s)-1)))
print(len(set(filter(f, range(254032,789860+1)))))
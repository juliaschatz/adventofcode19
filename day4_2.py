#!/usr/bin/python

ct = 0
for i in range(254032,789860+1):
    s = str(i)
    if ''.join(sorted(s)) == s:
        blks = []
        accum = s[0]
        for j in range(len(s)-1):
            if s[j] == s[j+1]:
                accum += s[j+1]
            else:
                blks += [accum]
                accum = s[j+1]
            if j == len(s)-2:
                blks += [accum]
        print(f"{s} {blks}")
        if not any(filter(lambda x: x==2, map(len, blks))):
            continue
    else:
        continue
    ct+=1
print(ct)
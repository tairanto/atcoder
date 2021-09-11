#!/usr/bin/python3

s=list(input())
r,l=[0],[0]
for i in s:
    if i=="<":
        r.append(r[-1]+1)
    else:
        r.append(0)
for i in reversed(s):
    if i==">":
        l.append(l[-1]+1)
    else:
        l.append(0)
print(sum([max(r[i],l[-1-i])for i in range(len(s)+1)]))

#!/usr/bin/python3

from collections import deque
d = deque()
N=int(input())
for i in range(N):
    t,x=map(int,input().split())
    if t==1:
        d.appendleft(x)
    elif t==2:
        d.append(x)
    else:
        print(d[x-1])
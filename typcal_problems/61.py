#!/usr/bin/python3


from collections import deque

Q=int(input())
d = deque()
for i in range(Q):
    t,x=map(int,input().split())
    if t==1:
        d.appendleft(x)
    if t==2:
        d.append(x)
    if t==3:
        print(d[x-1])
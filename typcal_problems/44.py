#!/usr/bin/python3

N,Q=map(int,input().split())
A=[*map(int,input().split())]
now=1
for i in range(Q):
    t,x,y=map(int,input().split())
    if t==1:
        A[(x-now)%N],A[(y-now)%N]=A[(y-now)%N],A[(x-now)%N]
    if t==2:
        now+=1
    if t==3:
        print(A[(x-now)%N])
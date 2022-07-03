#!/usr/bin/python3

N,Q=map(int,input().split())
s=list(input())
now=-1
for i in range(Q):
    q,x=map(int,input().split())
    if q==1:
        now-=x
    else:
        print(s[(now+x)%N])
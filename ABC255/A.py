#!/usr/bin/python3

N,K=map(int,input().split())
A=set(map(int,input().split()))
a,b=[],[]
for i in range(N):
    if i+1 in A:
        a.append([*map(int,input().split())])
    else:
        b.append([*map(int,input().split())])
ans=0
for x,y in b:
    m=float("inf")
    for X,Y in a:
        m=min(m,(X-x)**2+(Y-y)**2)
    ans=max(ans,m)
print(ans**0.5)
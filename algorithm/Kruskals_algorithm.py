#!/usr/bin/python3

import sys
sys.setrecursionlimit(10**9)
def find(x):
    if p[x]==-1:return x
    else:
        p[x]=find(p[x])
        return p[x]
 
def unite(x,y):
    x=find(x)
    y=find(y)
    if x==y:return
    if r[x]>r[y]:
        x,y=y,x
    r[y]+=r[x] #数数えられる
    p[x]=y
 
N,M=map(int,input().split())
p=[-1 for i in range(N+1)]
r=[1 for i in range(N+1)]

d=[]
from heapq import heappush,heappop
for i in range(M):
    a,b,c=map(int,input().split())
    heappush(d,(c,a,b))

ans=0
while d:
    cost,x,y=heappop(d)
    if find(x)!=find(y):
        unite(x,y)
        ans+=cost
print(ans)
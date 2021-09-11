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
    if r[x]==r[y]:
        r[y]+=1
    p[x]=y

n,m=map(int,input().split())
p=[-1 for i in range(n)]
r=[1 for i in range(n)]
same=[]
for i in range(m):
    a,b=map(int,input().split())
    if find(a-1)==find(b-1):
        same.append(a-1)
    unite(a-1,b-1)
print(p.count(-1)-len(set([find(i) for i in same])))
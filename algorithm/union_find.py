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
    p[x]=y

n,m=map(int,input().split())
x=[list(map(int,input().split())) for i in range(m)]
p=[-1 for i in range(n)]
for i in x:
    unite(i[0]-1,i[1]-1)

print(len(set([find(i) for i in range(n)])))
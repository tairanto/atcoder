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
uf=[[*map(int,input().split())] for i in range(m)]
ans=0
for i in range(m):
    p=[-1 for j in range(n)]
    r=[1 for j in range(n)]
    for j in range(m):
        if i==j:continue
        unite(uf[j][0]-1,uf[j][1]-1)
    if find(uf[i][0]-1)!=find(uf[i][1]-1):
        ans+=1
print(ans)
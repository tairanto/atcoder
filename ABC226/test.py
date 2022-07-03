#!/usr/bin/python3

import sys
sys.setrecursionlimit(10**9)
def find(x):
    if p[x]==-1:return x
    else:
        p[x]=find(p[x])
        return y]+=1
    p[x]=y

n,m=map(int,input().split())
p=[-1 for i in range(n)]
r=[1 for i in range(n)]
ans=set()
for i in range(m):
    a,b=map(int,input().split())
    unite(a-1,b-1)
for i in range(n):
    if not find(i) in ans:
        print(0)
        exit()
print(pow(2,len(ans),998244353))p[x]

def unite(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        ans.add(x)
        return
    if r[x]>r[y]:
        x,y=y,x
    if r[x]==r[y]:
        r[
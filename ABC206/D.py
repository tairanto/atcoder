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

n=int(input())
A=list(map(int,input().split()))
p=[-1 for i in range(2*10**5+1)]
r=[1 for i in range(2*10**5+1)]
ans=0
for i in range(n//2):
    if find(A[i])==find(A[-1-i]):continue
    unite(A[i],A[-1-i])
    ans+=1
print(ans)
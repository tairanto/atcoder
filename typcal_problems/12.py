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

H,W=map(int,input().split())
p=[-1 for i in range(H*W+1)]
r=[1 for i in range(H*W+1)]
grid=[[0 for i in range(W+1)]for j in range(H+1)]
x,y=[0,0,1,-1],[1,-1,0,0]
Q=int(input())
for i in range(Q):
    q=list(map(int,input().split()))
    if q[0]==1:
      grid[q[1]-1][q[2]-1]=1
      for j in range(4):
        if grid[q[1]-1+x[j]][q[2]-1+y[j]]:
          unite((q[1]-1)*W+q[2]-1,(q[1]-1+x[j])*W+q[2]-1+y[j])
    else:
      if grid[q[1]-1][q[2]-1] and grid[q[3]-1][q[4]-1] and find((q[1]-1)*W+q[2]-1)==find((q[3]-1)*W+q[4]-1):
        print("Yes")
      else:
        print("No")
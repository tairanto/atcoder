#!/usr/bin/python3


import sys
sys.setrecursionlimit(10**9)
ans=0
def check(v):
    global ans
    if checked[v]:return
    if come[v]:
        tmp=C[v]
        now=X[v]
        while now!=v:
            tmp =min(tmp,C[now])
            now=X[now]
        ans+=tmp
        return
    come[v]=1
    check(X[v])
    checked[v]=1


N=int(input())
X=[-1]+[*map(int,input().split())]
C=[-1]+[*map(int,input().split())]

checked=[0 for i in range(N+1)]
come = [0 for i in range(N+1)]

for i in range(1,N+1):
    check(i)

print(ans)
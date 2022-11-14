#!/usr/bin/python3

#pypyだと遅い

from sys import setrecursionlimit
setrecursionlimit(10**9)
def dfs(x):
    come[x]=1
    for i in edge[x-1]:
        if come[i]:continue
        dfs(i)
    return

N,M=map(int,input().split())
edge=[[] for i in range(N)]
for i in range(M):
    a,b=map(int,input().split())
    edge[a-1].append(b)
    edge[b-1].append(a)
come=[0]*(N+1)
dfs(1)
print("The graph is connected." if sum(come)==N else "The graph is not connected.")
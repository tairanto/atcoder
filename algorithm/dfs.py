#!/usr/bin/python3

#pypyだと遅い
import sys
sys.setrecursionlimit(10**9)
def dfs(v,ptr):
    seen[v-1] = 1
    ptr+=1
    for i in G[v]:
        if seen[i-1]:continue
        ptr=dfs(i, ptr)
    return ptr

N,M=map(int,input().split())
G={i+1:[] for i in range(N)}
for i in range(M):
    a,b=map(int,input().split())
    G[a].append(b)
ans=0
for i in range(1,N+1):
    seen=[0 for i in range(N)]
    ptr=0
    ans+=dfs(i,ptr)
print(ans)
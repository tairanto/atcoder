#!/usr/bin/python3
import sys
sys.setrecursionlimit(10**9)

def dfs(now):
    ans.append(now)
    seen[now]=1
    for i in G[now]:
        if seen[i]:continue
        dfs(i)
        ans.append(now)

N=int(input())
G={i+1:[] for i in range(N)}
ans=[0]
for i in range(N-1):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)
for i in G:
    G[i].sort()
seen=[0 for i in range(N+1)]
dfs(1)
print(*ans[1:])
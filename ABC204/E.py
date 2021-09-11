#!/usr/bin/python3

import sys
sys.setrecursionlimit(10**9)
from copy import deepcopy
def dfs(v,ans):
    if v==N and ans[-1][0]>path[-1][0]:
        ans=deepcopy(path[1:])
    seen[v-1] = 1
    for i in G[v]:
        if seen[i[0]-1]:continue
        path.append([path[-1][3]+i[1]+(0<i[2])]+i)
        ans=dfs(i[0],ans)
    path.pop(-1)
    seen[v-1]=0
    return ans

N,M=map(int,input().split())
G={i+1:[] for i in range(N)}
for i in range(M):
    a,b,c,d=map(int,input().split())
    G[a].append([b,c,d])
seen=[0 for i in range(N)]
path=[[0,0,0,0]]
ans=[[float("inf"),0,0,0]]
ans=dfs(1,ans)
now=len(ans)
cnt=0
before=10**9
while now>0:
    
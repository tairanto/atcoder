#!/usr/bin/python3


N=int(input())
G={i+1:[] for i in range(N)}
for i in range(N-1):
    a,b,c=map(int,input().split())
    G[a].append([b,c])
    G[b].append([a,c])
Q,K=map(int,input().split())
xy=[[*map(int,input().split())] for i in range(Q)]
ans=[0 for i in range(N+1)]
seen=[0 for i in range(N+1)]

from collections import deque
d=deque([K])
seen[K]=1
while d:
    D=d.popleft()
    for i in G[D]:
        a,c=i
        if seen[a]:continue
        seen[a]=1
        ans[a]=ans[D]+c
        d.append(a)
for x,y in xy:
    print(ans[x]+ans[y])
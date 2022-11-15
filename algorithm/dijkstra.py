#!/usr/bin/python3

def dijkstra(s):
    dist=[INF]*(N+1)
    dist[s]=0
    pq=[(0,s)]
    while pq:
        c,t=heappop(pq)
        if dist[t]<c:continue
        for T,C in edge[t]:
            if c+C<dist[T]:
                dist[T]=c+C
                heappush(pq,(c+C,T))
    return dist

from heapq import heappush,heappop
INF=float("inf")
N,M=map(int,input().split())
edge=[[] for _ in range(N+1)]

for i in range(M):
    a,b,c=map(int,input().split())
    edge[a].append((b,c))
    edge[b].append((a,c))

start=dijkstra(1)
end=dijkstra(N)
for i in range(1,N+1):
    print(start[i]+end[i])
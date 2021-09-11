#!/usr/bin/python3

N,Q=map(int,input().split())
G={i+1:[] for i in range(N)}
for i in range(N):
    a,b=map(int,input().split())
    G[a].append(b)
    G[b].append(a)

for i in range(Q):
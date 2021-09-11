#!/usr/bin/python3

n,m=map(int,input().split())
graph={i+1:set() for i in range(n)}
for i in range(m):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

for i in graph[1]:
    if n in graph[i]:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
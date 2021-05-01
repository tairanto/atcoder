#!/usr/bin/python3
n,m=map(int,input().split())
graph={i+1:[] for i in range(n)}
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    if len(graph[i+1])==0:
        print(0)
        continue
    ans=set()
    for j in graph[i+1]:
        ans|=set(graph[j]+[j])
    print(len(ans)-len(graph[i+1])-1)
#!/usr/bin/python3

5
1 2
2 3
3 4
3 5
n=int(input())
graph={i+1:[] for i in range(n)}
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a]=[b,0]
    graph[b]=[a,0]
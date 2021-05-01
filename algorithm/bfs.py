#!/usr/bin/python3
n,k=map(int,input().split())
graph={i+1:[] for i in range(n)}
for i in range(k):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
import queue
que=queue.Queue()
que.put(1)
seen=[1]+[0 for i in range(n-1)]
ans=[0 for i in range(n)]
cnt=[n for i in range(n)]
while not que.empty():
    x=que.get()
    for i in graph[x]:
        if seen[i-1]:continue
        seen[i-1]=1
        ans[i-1]=x
        que.put(i)
print("Yes",*ans[1:],sep="\n")
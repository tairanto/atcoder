#!/usr/bin/python3
n=int(input())
G={i+1:[] for i in range(n)}
for i in range(n-1):
    a,b,w=map(int,input().split())
    G[a].append([b,w])
    G[b].append([a,w])

import queue
que=queue.Queue()
que.put([1,0])
seen=[1]+[0 for i in range(n-1)]
ans=[0]+[-1 for i in range(n-1)]
while not que.empty():
    x,W=que.get()
    for i,nw in G[x]:
        if seen[i-1]:continue
        seen[i-1]=1
        que.put([i,W+nw])
        if nw%2:
            ans[i-1]=(ans[x-1]+1)%2
        else:
            ans[i-1]=ans[x-1]
print(*ans,sep="\n")
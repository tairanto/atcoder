#!/usr/bin/python3

from collections import deque

d = deque()
now={}
N,K=map(int,input().split())
A=[*map(int,input().split())]
i=0
ans=0
while i<N:
    d.append(A[i])
    if not A[i] in now:
        now[A[i]]=0
    now[A[i]]+=1
    if len(now)<=K:
        ans=max(ans,len(d))
    else:
        while len(now)>K:
            r=d.popleft()
            now[r]-=1
            if now[r]==0:
                now.pop(r)
    i+=1
print(ans)
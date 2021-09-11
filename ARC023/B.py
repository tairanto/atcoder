#!/usr/bin/python3

R,C,D=map(int,input().split())
A=[[*map(int,input().split())] for _ in range(R)]
from collections import deque
d=deque([[0,0,0,A[0][0]]])
ans=0
while d:
    x,y,cnt,score=d.popleft()
    if D%2==cnt%2:
        ans=max(ans,score)
    if cnt+1>D:continue
    if x+1<R and A[x+1][y]:
        d.append([x+1,y,cnt+1,A[x+1][y]])
        A[x+1][y]=0
    if y+1<C and A[x][y+1]:
        d.append([x,y+1,cnt+1,A[x][y+1]])
        A[x][y+1]=0
print(ans)
#!/usr/bin/python3

def check(X,Y):
    if grid[X][Y]==".":
        grid[X][Y]=grid[x][y]+1
        d.append([X,Y])
    return

H,W=map(int,input().split())
S=list(map(int,input().split()))
G=list(map(int,input().split()))
grid=[list(input()) for i in range(H)]
from collections import deque
S=[S[0]-1,S[1]-1]
d=deque([S])
grid[S[0]][S[1]]=0
while d:
    x,y=d.popleft()
    x1,x2,y1,y2=x-1,x+1,y-1,y+1
    check(x1,y)
    check(x2,y)
    check(x,y1)
    check(x,y2)
print(grid[G[0]-1][G[1]-1])
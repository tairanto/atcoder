#!/usr/bin/python3

N=int(input())
grid=[[0 for i in range(1000+1)]for j in range(1000+1)]
ans=[0 for i in range(N+1)]
for i in range(N):
    x1,y1,x2,y2=map(int,input().split())
    grid[x1][y1]+=1
    grid[x2][y1]-=1
    grid[x1][y2]-=1
    grid[x2][y2]+=1
x=[0 for i in range(1000+1)]
for i in range(1000+1):
    now=0
    for j in range(1000+1):
        now+=grid[i][j]
        x[j]+=now
        ans[x[j]]+=1
print(*ans[1:],sep="\n")
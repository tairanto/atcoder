#!/usr/bin/python3
h,w=map(int,input().split())
grid=[list(input()) for i in range(h)]
r=[[0 for i in range(w+1)]for j in range(h+1)]
l=[[0 for i in range(w+1)]for j in range(h+1)]
u=[[0 for i in range(w+1)]for j in range(h+1)]
d=[[0 for i in range(w+1)]for j in range(h+1)]
for i in range(h):
    for j in range(w):
        if grid[i][j]=="#":
            r[i+1][j+1]=0
            d[i+1][j+1]=0
        else:
            r[i+1][j+1]=r[i+1][j]+1
            d[i+1][j+1]=d[i][j+1]+1
for i in range(h):
    for j in range(w):
        if grid[h-i-1][w-j-1]=="#":
            l[h-i-1][w-j-1]=0
            u[h-i-1][w-j-1]=0
        else:
            l[h-i-1][w-j-1]=l[h-i][w-j-1]+1
            u[h-i-1][w-j-1]=u[h-i-1][w-j]+1
ans=0
for i in range(h):
    for j in range(w):
        ans=max(ans,r[i+1][j+1]+l[i][j]+u[i][j]+d[i+1][j+1]-3)
print(ans)

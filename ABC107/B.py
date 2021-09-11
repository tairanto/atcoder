#!/usr/bin/python3


H,W=map(int,input().split())
grid=[list(input()) for i in range(H)]
tate=[1 if sum([1 for j in range(H) if grid[j][i]=="."])==H else 0 for i in range(W)]
yoko=[1 if sum([1 for j in grid[i] if j=="."])==W else 0 for i in range(H)]
ans=[]
for i in range(H):
    temp=[]
    for j in range(W):
        if tate[j] or yoko[i]:continue
        temp.append(grid[i][j])
    if len(temp)==0:continue
    ans.append(temp)
for i in ans:
    print(*i,sep="")
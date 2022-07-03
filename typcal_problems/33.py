#!/usr/bin/python3


from threading import get_ident


H,W=map(int,input().split())
grid=[["." for i in range(W+1)]for j in range(H+1)]
ans=0
if H==1 or W==1:
    print(H*W)
    exit()
for i in range(H):
    for j in range(W):
        flag=0
        for x in range(-1,1,1):
            for y in range(-1,1,1):
                if grid[i+x][j+y]=="#":
                    flag=1
                    break
            if flag:break
        if not flag:
            ans+=1
            grid[i][j]="#"
print(ans)
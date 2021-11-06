#!/usr/bin/python3


H,W=map(int,input().split())
a=[[*map(int,input().split())] for _ in range(H)]
ans=[]
for i in range(H):
    for j in range(W):
        if i+1==H and j+1==W:continue
        if a[i][j]%2:
            if i+1==H:
                a[i][j+1]+=1
                ans.append([i+1,j+1,i+1,j+2])
            else:
                a[i+1][j]+=1
                ans.append([i+1,j+1,i+2,j+1])
print(len(ans))
for i in ans:
    print(*i)
#!/usr/bin/python3

def hou(x1,y1,x2,y2,H,W):
    temp=float("inf")
    if x1>=0 and y2<W:
        temp=min(temp,A[x1][y2])
    if x2<H and y2<W:
        temp=min(temp,A[x2][y2])
    return temp

H,W,C=map(int,input().split())
A=[list(map(int,input().split())) for i in range(H)]
ans=float("inf")
for i in range(H):
    for j in range(W):
        R=max(H-i+j,H-i+W-j)
        for k in range(1,R+1):
            if k*C+A[i][j]>ans:break
            ans=min(ans,min([A[i][j]+k*C+hou(i-l,j-k+l,i+l,j+k-l,H,W) for l in range(k+1)]))
print(ans)
#!/usr/bin/python3

H,W=map(int,input().split())
c=[[*map(int,input().split())] for _ in range(10)]
A=[[*map(int,input().split())] for _ in range(H)]
seen=[0 for _ in range(10)]

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k] + c[k][j])
ans=0
for i in range(H):
    for j in range(W):
        if A[i][j]+1:
            ans+=c[A[i][j]][1]
print(ans)
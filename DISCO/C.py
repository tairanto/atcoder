#!/usr/bin/python3

H,W,K=map(int,input().split())
s=[list(input()) for i in range(H)]
for i in range(H):
    for j in range(W):
        if s[i][j]==".":
            s[i][j]=0
        else:
            s[i][j]=K
            K-=1
for i in range(H):
    x=0
    for j in range(W):
        if s[i][j]==0:
            s[i][j]=x
        else:
            x=s[i][j]
    for j in range(W-1,-1,-1):
        if s[i][j]==0:
            s[i][j]=x
        else:
            x=s[i][j]
for j in range(W):
    x=0
    for i in range(H):
        if s[i][j]==0:
            s[i][j]=x
        else:
            x=s[i][j]
    for i in range(H-1,-1,-1):
        if s[i][j]==0:
            s[i][j]=x
        else:
            x=s[i][j]
for i in s:
    print(*i)_
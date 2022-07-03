#!/usr/bin/python3

H,W=map(int,input().split())
s=[list(input()) for i in range(H)]
ans=[]
for i in range(H):
    for j in range(W):
        if s[i][j]=="o":
            ans.append([i,j])
print(abs(ans[0][0]-ans[1][0])+abs(ans[0][1]-ans[1][1]))
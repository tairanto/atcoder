#!/usr/bin/python3

H,W=map(int,input().split())
s=[list(input()) for i in range(H)]
dp=[[float("inf") for i in range(W)] for j in range(H)]
dp[0][0]=int(s[0][0]=="#")
for i in range(H):
    for j in range(W):
        if i+1<H:
            dp[i+1][j]=min(dp[i+1][j],dp[i][j]+(s[i+1][j]!=[".","#"][dp[i][j]%2]))
        if j+1<W:
            dp[i][j+1]=min(dp[i][j+1],dp[i][j]+(s[i][j+1]!=[".","#"][dp[i][j]%2]))
print(dp[-1][-1]//2+dp[-1][-1]%2)
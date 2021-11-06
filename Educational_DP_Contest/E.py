#!/usr/bin/python3

N,W=map(int,input().split())
dp=[[float("inf") for i in range(10**5+1)]for j in range(N+1)]
dp[0][0]=0
for i in range(N):
    w,v=map(int,input().split())
    for j in range(10**5+1):
        if j+v<=100000:dp[i+1][j+v]=min(dp[i+1][j+v],dp[i][j]+w)
        dp[i+1][j]=min(dp[i+1][j],dp[i][j])
for i in range(10**5,-1,-1):
    if dp[-1][i]<=W:
        print(i)
        exit()
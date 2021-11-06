#!/usr/bin/python3

N=int(input())
dp=[[0 for j in range(3)] for i in range(N+1)]
for i in range(N):
    a,b,c=map(int,input().split())
    for j in range(3):
        for k in range(1,3):
            dp[i+1][(j+k)%3]=max(dp[i+1][(j+k)%3],dp[i][j]+[a,b,c][(j+k)%3])
print(max(dp[-1]))
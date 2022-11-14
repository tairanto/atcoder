#!/usr/bin/python3

N,Q=map(int,input().split())
A=[*map(int,input().split())]
dp=[[A[i]] for i in range(N)]
for i in range(30):
    for j in range(N):
        next=dp[j][i]
        dp[j].append(dp[next-1][i])

for i in range(Q):
    x,y=map(int,input().split())
    for bit in range(30):
        if (y>>bit)%2==0:continue
        x=dp[x-1][bit]
    print(x)
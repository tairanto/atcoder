#!/usr/bin/python3


N=int(input())
A=[*map(int,input().split())]
dp=[float("inf"),float("inf")]
for i in range(N):
    dp[0]=min(dp[0]+A[])
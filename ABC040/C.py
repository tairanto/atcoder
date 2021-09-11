#!/usr/bin/python3


N=int(input())
L=list(map(int,input().split()))+[0,0]
dp=[float("inf") for _ in range(N+2)]
dp[0]=0
for i in range(N):
  dp[i+1]=min(dp[i+1],dp[i]+abs(L[i+1]-L[i]))
  dp[i+2]=dp[i]+abs(L[i+2]-L[i])
print(dp[-3])
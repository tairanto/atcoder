#!/usr/bin/python3

S=int(input())
dp=[0 for i in range(S+1)]
dp[0]=1
mod=10**9+7
for i in range(1,S+1):
  for j in range(i-3+1):
    dp[i]=(dp[i]+dp[j])%mod
print(dp[S],dp)
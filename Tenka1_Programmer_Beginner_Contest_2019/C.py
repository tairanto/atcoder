#!/usr/bin/python3


N,S=int(input()),list(input())
dp=[[0,0] for i in range(N+1)]#0->.埋め1->#埋め始めてる
for i in range(N):
    if S[i]=="#":
        dp[i+1][0]=dp[i][0]+1
        dp[i+1][1]=min(dp[i])
    else:
        dp[i+1][0]=dp[i][0]
        dp[i+1][1]=min(dp[i])+1
print(min(dp[-1]))


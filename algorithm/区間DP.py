#!/usr/bin/python3

N=int(input())
P=[[*map(int,input().split())] for _ in range(N)]
dp=[[0]*(N+1) for _ in range(N+1)]

now=N-1
while now>0:
    for i in range(1,N-now+1):
        l,r=i,i+now
        if l+1<=P[l-1][0]<=r:
            dp[l+1][r]=max(dp[l+1][r],dp[l][r]+P[l-1][1])
        else:
            dp[l+1][r]=max(dp[l+1][r],dp[l][r])
        if l<=P[r-1][0]<=r-1:
            dp[l][r-1]=max(dp[l][r-1],dp[l][r]+P[r-1][1])
        else:
            dp[l][r-1]=max(dp[l][r-1],dp[l][r])
    now-=1
ans=0
for i in range(N+1):
    ans=max(dp[i][i],ans)
print(ans)
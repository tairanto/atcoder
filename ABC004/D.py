#!/usr/bin/python3

R,G,B=map(int,input().split())
dp=[float("inf") for j in range(R+G+B)]+[0]
for i in range(2000):
    temp=[0 for j in range(R+G+B+1)]
    for j in range(R+G+B):
        if j<R:
            cost=i-900
        elif j<R+G:
            cost=i-1000
        else:
            cost=i-1100
        temp[-2-j]=min(dp[-2-j],dp[-1-j]+abs(cost))
    dp,temp=temp,dp
print(dp[0])
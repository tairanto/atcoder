#!/usr/bin/python3

N=int(input())
R=[*map(int,input().split())]
dp=[[1,1] for i in range(N)]#up,down
for i in range(N):
    for j in range(i+1,N):
        if R[i]<R[j]:
            dp[j][0]=max(dp[j][0],dp[i][1]+1)
        if R[i]>R[j]:
            dp[j][1]=max(dp[j][1],dp[i][0]+1)
if max(dp[-1])>2:
    print(max(dp[-1]))
else:
    print(0)
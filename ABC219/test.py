#!/usr/bin/python3

N=int(input())
X,Y=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(N)]
dp=[[[0,0,set()] for i in range(N)]for j in range(N+1)]
import copy
for i in range(N):#個数
    for j in range(N):#今見てるところ
        for k in range(N):#前のところ
            if j in dp[i][k][2]:continue
            if dp[i][k][0]+ab[j][0]>dp[i+1][j][0] and dp[i][k][1]+ab[j][1]>dp[i+1][j][1]:
                dp[i+1][j][0]=dp[i][k][0]+ab[j][0]
                dp[i+1][j][1]=dp[i][k][1]+ab[j][1]
                dp[i+1][j][2]=copy.copy(dp[i][k][2])
                dp[i+1][j][2].add(j)
        if dp[i+1][j][0]>=X and dp[i+1][j][1]>=Y:
            print(i+1)
            exit()
print(-1)
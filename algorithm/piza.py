#!/usr/bin/python3
n,k=map(int,input().split())
x=[list(map(int,input().split())) for i in range(k)]
dp=[[[0 for k in range(3)] for j in range(3)] for i in range(n-1)]
x.sort()
#２日目まで
cnt=0
if cnt<k and x[cnt][0]==1:
    dp[0][x[cnt][1]-1][0]=1
    cnt+=1
else:
    for i in range(3):
        dp[0][i][0]=1
if cnt<k and x[cnt][0]==2:
    for i in range(3):
        if x[cnt][1]==1:continue
        dp[0][i][x[cnt][1]-1]+=dp[0][i][0]
        dp[0][i][0]=0
    cnt+=1
else:
    for i in range(3):
        for j in range(2):
            dp[0][i][j+1]+=dp[0][i][0]
#3日目以降
for i in range(n-2):
    L=[0,1,2]
    if cnt<k and x[cnt][0]==i+3:
        dp[i][x[cnt][1]-1][x[cnt][1]-1]=0
        L=[x[cnt][1]-1]
        cnt+=1
    for j in range(3):
        for m in range(3):
            for l in L:
                if j==m==l:continue
                dp[i+1][m][l]=(dp[i+1][m][l]+dp[i][j][m])%10000
print(sum([sum(i) for i in dp[-1]])%10000)
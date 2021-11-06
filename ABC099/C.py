#!/usr/bin/python3

six,nine=[pow(6,i) for i in range(1,7)],[pow(9,i) for i in range(1,6)]
dp=[i for i in range(10**5+1)]
for i in range(1,10**5+1):
    for j in six:
        if i-j>=0:
            dp[i]=min(dp[i],dp[i-j]+1)
    for j in nine:
        if i-j>=0:
            dp[i]=min(dp[i],dp[i-j]+1)
print(dp[int(input())])
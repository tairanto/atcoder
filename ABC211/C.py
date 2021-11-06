#!/usr/bin/python3

S=input()
memo={"c":0,"h":1,"o":2,"k":3,"u":4,"d":5,"a":6,"i":7}
dp=[0 for i in range(8)]
mod=10**9+7
for i in S:
    if i=="c":
        dp[0]+=1
    elif i in memo:
        dp[memo[i]]=(dp[memo[i]]+dp[memo[i]-1])%mod
print(dp[-1])
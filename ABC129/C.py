#!/usr/bin/python3
n,m=map(int,input().split())
x=[int(input()) for i in range(m)]
mod=10**9+7
dp=[0,1]
flag=-1
for i in range(1,n+1):
    if m>0 and x[0]==i:
        m-=1
        x.pop(0)
        if flag==i-1:
            print(0)
            exit()
        else:
            dp.append(0)
            flag=i
    else:
        dp.append((dp[i-1]+dp[i])%mod)
print(dp[-1])
#!/usr/bin/python3
mod=10**9+7
n,p=map(int,input().split())
ans=p-1
p10=1
for i in range(10):
    p10=p10*(p-2)%mod
for i in range((n-1)//10):
    ans=(ans*p10)%mod
for i in range((n-1)%10):
    ans=(ans*(p-2))%mod

print(ans)
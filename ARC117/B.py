#!/usr/bin/python3


n=int(input())
x=list(map(int,input().split()))+[0]
x.sort()
ans=1
mod=10**9+7
for i in range(n):
    ans=ans*(x[i+1]-x[i]+1)%mod
print(ans%mod)
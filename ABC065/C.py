#!/usr/bin/python3
mod=10**9+7
p=[1]
for i in range(2,10**5+1):
    p.append((p[-1]*i)%mod)

n,m=map(int,input().split())
if abs(n-m)>=2:
    print(0)
elif abs(n-m)==1:
    print(p[n-1]*p[m-1]%mod)
else:
    print(2*p[n-1]*p[m-1]%mod)
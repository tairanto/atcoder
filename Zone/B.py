#!/usr/bin/python3
n,d,h=map(int,input().split())
ans=0
for i in range(n):
    di,hi=map(int,input().split())
    ans=max(ans,h-d*(h-hi)/(d-di))
print(ans)
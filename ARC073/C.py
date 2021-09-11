#!/usr/bin/python3


n,t=map(int,input().split())
x=list(map(int,input().split()))
ans=t
for i in range(n-1):
    if x[i+1]-x[i]<t:
        ans+=x[i+1]-x[i]
    else:
        ans+=t
print(ans)
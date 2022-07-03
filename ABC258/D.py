#!/usr/bin/python3

N,X=map(int,input().split())
now=0
ans=float("inf")
for i in range(min(N,X)):
    a,b=map(int,input().split())
    now+=a+b
    ans=min(ans,now+(X-i-1)*b)
print(ans)
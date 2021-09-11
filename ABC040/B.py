#!/usr/bin/python3

n=int(input())
ans=float("inf")
for i in range(1,1001):
    for j in range(1,1001):
        if i*j>n:continue
        ans=min(ans,abs(i-j)+n-i*j)
print(ans)
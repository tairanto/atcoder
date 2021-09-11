#!/usr/bin/python3


n=int(input())
A=list(map(int,input().split()))
ans=0
for i in A:
    ans+=max(i-10,0)
print(ans)
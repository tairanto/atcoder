#!/usr/bin/python3

n=int(input())
A=[*map(int,input().split())]
total=sum(A)
ans=0
for i in A:
    ans+=(total>3)
    total-=i
print(ans)
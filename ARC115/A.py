#!/usr/bin/python3

n,m=map(int,input().split())
odd,even=0,0
for i in range(n):
    s=list(input())
    if s.count("1")%2:
        odd+=1
    else:
        even+=1
print(odd*even)
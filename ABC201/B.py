#!/usr/bin/python3
n=int(input())
m=[]
for i in range(n):
    name,h=input().split()
    m.append([int(h),name])
m.sort()
print(m[-2][1])
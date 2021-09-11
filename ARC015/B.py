#!/usr/bin/python3

n=int(input())
a=[0 for i in range(6)]
for i in range(n):
    Mt,mt=map(float,input().split())
    if Mt>=35:a[0]+=1
    if 30<=Mt<35:a[1]+=1
    if 25<=Mt<30:a[2]+=1
    if mt>=25:a[3]+=1
    if Mt>=0 and mt<0:a[4]+=1
    if Mt<0:a[5]+=1
print(*a)
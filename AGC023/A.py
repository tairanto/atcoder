#!/usr/bin/python3

N=int(input())
num={0:1}
now=0
for i in map(int,input().split()):
    now+=i
    if not now in num:
        num[now]=0
    num[now]+=1
print(sum([(num[i]-1)*num[i]//2 for i in num]))
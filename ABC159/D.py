#!/usr/bin/python3

n=int(input())
x=list(map(int,input().split()))
num={}
for i in x:
    if not i in num:
        num[i]=0
    num[i]+=1
total=sum([num[i]*(num[i]-1)//2 for i in num])
for i in x:
    print(total-num[i]+1)
#!/usr/bin/python3

n=int(input())
x=list(map(int,input().split()))
cnt,num=0,{}
for i in x:
    if not i in num:
        num[i]=0
    num[i]+=1
for i in num:
    if i>num[i]:
        cnt+=num[i]
    if num[i]>i:
        cnt+=num[i]-i
print(cnt)
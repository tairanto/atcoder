#!/usr/bin/python3

n=int(input())
num={}
A=list(map(int,input().split()))
for i in A:
    if not i in num:
        num[i]=0
    num[i]+=1
ans=0
for i in A:
    ans+=n-1-(num[i]-1)
    num[i]-=1
    n-=1
print(ans)
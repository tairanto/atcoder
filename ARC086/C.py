#!/usr/bin/python3


n,k=map(int,input().split())
x=list(map(int,input().split()))
num={}
for i in x:
    if not i in num:
        num[i]=0
    num[i]+=1
N=len(num)
if N<=k:
    print(0)
else:
    L=list(num.values())
    L.sort()
    print(sum(L[:N-k]))

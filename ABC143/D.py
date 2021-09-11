#!/usr/bin/python3

n=int(input())
L=list(map(int,input().split()))
num=[0 for i in range(2001)]
for i in L:num[i]+=1
for i in range(1,2001):num[i]+=num[i-1]
ans=0
L.sort()
for i in range(n):
    for j in range(i+1,n):
        ans+=num[L[i]+L[j]-1]-num[L[j]-L[i]]
        if L[j]-L[i]<L[i]<L[i]+L[j]:ans-=1
        if L[j]-L[i]<L[j]<L[i]+L[j]:ans-=1
print(ans//3)
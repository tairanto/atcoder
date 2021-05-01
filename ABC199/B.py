#!/usr/bin/python3
n=int(input())
a,b=list(map(int,input().split())),list(map(int,input().split()))
num=[0 for i in range(1001)]
for i in range(n):
    x,y=a[i],b[i]
    for j in range(x,y+1):
        num[j]+=1
print(sum([1 for i in num if i==n]))
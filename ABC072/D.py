#!/usr/bin/python3

n=int(input())
a=list(map(int,input().split()))
cnt=0
for i in range(n-1):
    if a[i]==i+1:
        a[i+1]=-1
        cnt+=1
print(cnt+(n==a[-1]))
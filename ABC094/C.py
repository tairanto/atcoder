#!/usr/bin/python3


n=int(input())
x=list(map(int,input().split()))
y=sorted(x)
a=[y[n//2-1],y[n//2]]
for i in x:
    if i<=a[0]:
        print(a[1])
    else:
        print(a[0])
#!/usr/bin/python3

n,k=map(int,input().split())
now=0
for i in range(n):
    a,b=map(int,input().split())
    if a-now>k:
        print(now+k)
        exit()
    else:
        k=k-(a-now)+b
        now=a

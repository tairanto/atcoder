#!/usr/bin/python3

n,k=map(int,input().split())
now=0
ab=[list(map(int,input().split())) for i in range(n)]
ab.sort()
for i in range(n+1):
    if i==n:
        print(now+k)
        exit()
    a,b=ab[i][0],ab[i][1]
    if a-now>k:
        print(now+k)
        exit()
    else:
        k=k-(a-now)+b
        now=a

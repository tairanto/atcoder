#!/usr/bin/python3

n,m=map(int,input().split())
CD={i+1:i+1 for i in range(n)}
CD[0]=-1
now=0
for i in range(m):
    disk=int(input())
    CD[now]=CD[disk]
    now=disk
    CD[disk]=-1
for i in range(1,n+1):
    for j in CD:
        if CD[j]==i:
            print(j)
            break

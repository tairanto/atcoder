#!/usr/bin/python3
n,d=map(int,input().split())
x=[list(map(int,input().split())) for i in range(n)]
cnt=0
for i in range(n):
    for j in range(i+1,n):
        dist=sum([pow(x[i][k]-x[j][k],2) for k in range(d)])
        if int(dist**0.5)**2==dist:
            cnt+=1
print(cnt)
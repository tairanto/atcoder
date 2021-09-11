#!/usr/bin/python3

N,D,K=map(int,input().split())
d=[[*map(int,input().split())] for _ in range(D)]
k=[[*map(int,input().split())] for _ in range(K)]
for i in range(K):
    now=k[i][0]
    for j in range(D):
        if k[i][0]<k[i][1]:
            if d[j][0]<=now<=d[j][1]:
                now=d[j][1]
                if now>=k[i][1]:break
        else:
            if d[j][0]<=now<=d[j][1]:
                now=d[j][0]
                if now<=k[i][1]:break
    print(j+1)
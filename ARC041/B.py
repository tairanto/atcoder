#!/usr/bin/python3


N,M=map(int,input().split())
b=[[*map(int,list(input()))] for _ in range(N)]
ans=[[0 for _ in range(M)]for _ in range(N)]

for i in range(1,N-1):
    for j in range(1,M-1):
        if b[i-1][j] and b[i][j-1] and b[i+1][j] and b[i][j+1]:
            m=min(b[i-1][j],b[i][j-1],b[i+1][j],b[i][j+1])
            ans[i][j]=m
            b[i-1][j]-=m
            b[i][j-1]-=m
            b[i+1][j]-=m
            b[i][j+1]-=m
for i in ans:
    print(*i,sep="")
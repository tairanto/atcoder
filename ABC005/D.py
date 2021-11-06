#!/usr/bin/python3

N=int(input())
D=[[*map(int,input().split())] for _ in range(N)]
c=[[0 for _ in range(N+1)]for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        c[i+1][j+1]=c[i+1][j]+c[i][j+1]-c[i][j]+D[i][j]
ans=[0 for i in range(N*N+1)]
for i in range(N):
    for j in range(N):
        for k in range(i,N):
            for l in range(j,N):
                ans[(k-i+1)*(l-j+1)]=max(ans[(k-i+1)*(l-j+1)],c[k+1][l+1]+c[i][j]-c[k+1][j]-c[i][l+1])
for i in range(int(input())):
    print(max(ans[:int(input())+1]))
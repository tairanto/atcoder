#!/usr/bin/python3

N,M=map(int,input().split())
wf=[[float("inf") for _ in range(N)]for _ in range(N)]
for i in range(M):
    a,b,t=map(int,input().split())
    wf[a-1][b-1]=t
    wf[b-1][a-1]=t

for i in range(N):
    wf[i][i]=0
for k in range(N):
    for i in range(N):
        for j in range(N):
            wf[i][j]=min(wf[i][j],wf[i][k]+wf[k][j])
print(min([max(wf[i])for i in range(N)]))
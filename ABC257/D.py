#!/usr/bin/python3

def dist(x1,x2):
    return abs(x1[0]-x2[0])+abs(x1[1]-x2[1])

N=int(input())
x=[[*map(int,input().split())] for i in range(N)]
d=[[dist(x[i],x[j])//x[i][2]+(dist(x[i],x[j])%x[i][2]>0) for j in range(N)]for i in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            d[i][j]=min(d[i][j],max(d[i][k],d[k][j]))#今回は訓練回数だから足さずに最大をとればいい
print(min([max(d[i]) for i in range(N)]))
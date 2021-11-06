#!/usr/bin/python3


N=int(input())
h=[*map(int,input().split())]+[0]
c=[float("inf") for i in range(N+1)]
c[0]=0
for i in range(N-1):
    c[i+1]=min(c[i+1],c[i]+abs(h[i]-h[i+1]))
    c[i+2]=min(c[i+2],c[i]+abs(h[i]-h[i+2]))
print(c[-2])
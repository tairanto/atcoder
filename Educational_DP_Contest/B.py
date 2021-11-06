#!/usr/bin/python3


N,K=map(int,input().split())
h=[*map(int,input().split())]+[0]*100
c=[float("inf") for i in range(N+100)]
c[0]=0
for i in range(N):
    for k in range(1,K+1):
        c[i+k]=min(c[i+k],c[i]+abs(h[i]-h[i+k]))
print(c[-101])
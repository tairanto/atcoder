#!/usr/bin/python3

N,x=map(int,input().split())
a=[*map(int,input().split())]+[0]
ans=0
for i in range(N):
    now=a[i]+a[i-1]
    if now>x:
        if now-x<=a[i]:
            a[i]-=now-x
        else:
            a[i-1]-=now-x+a[i]
            a[i]=0
        ans+=now-x
print(ans)
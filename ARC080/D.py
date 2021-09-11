#!/usr/bin/python3

H,W=map(int,input().split())
N=int(input())
a=list(map(int,input().split()))
now=0
for i in range(H):
    ans=[]
    for j in range(W):
        ans.append(now+1)
        a[now]-=1
        if a[now]==0:now+=1
    if i%2==0:print(*ans)
    else:print(*reversed(ans))
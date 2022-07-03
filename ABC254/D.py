#!/usr/bin/python3

N=int(input())
ans=0
for i in range(1,N+1):
    d=2
    now=i
    while d*d<=now:
        if now%(d*d)==0:now//=(d*d)
        else:d+=1
    d=1
    while now*d*d<=N:
        ans+=1
        d+=1
print(ans)
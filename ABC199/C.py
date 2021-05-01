#!/usr/bin/python3
n=int(input())
s=list(input())
q=int(input())
cnt=0
mod=2*n
for i in range(q):
    t,a,b=map(int,input().split())
    a=(a-1+n*cnt)%mod
    b=(b-1+n*cnt)%mod
    if t==1:
        s[a],s[b]=s[b],s[a]
    else:
        cnt+=1
if cnt%2==1:
    print(*s[n:],*s[:n],sep="")
else:
    print(*s,sep="")
#!/usr/bin/python3


N,R=map(int,input().split())
x=list(input())
ans=0
flag=0
i=0
while i<N:
    if flag==0 and x[-1-i]==".":
        ans=max(0,N-i-R)+1
        i+=R
        flag=1
    elif flag and x[-1-i]==".":
        ans+=1
        i+=R
    else:
        i+=1
print(ans)
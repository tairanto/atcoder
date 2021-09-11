#!/usr/bin/python3

n=int(input())
x=list(map(int,input().split()))
x.sort()
cnt,ans=0,0
if n%2:
    for i in range(-n,n+1):
        if i%2==0:
            ans+=x[cnt]*i
            cnt+=1
else:
    for i in range(-n,n+1):
        if i%2:
            ans+=x[cnt]*i
            cnt+=1
print(ans)
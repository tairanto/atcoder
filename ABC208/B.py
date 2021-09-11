#!/usr/bin/python3

P=int(input())
ans=0
now=1
for i in range(1,100):
    now*=i
    if now>=P:break
for j in range(i,0,-1):
    ans+=P//now
    P%=now
    now//=j
print(ans)
#!/usr/bin/python3

R,G,B,n=map(int,input().split())
ans=0
for r in range(n//R+1):
    if r*R>n:continue
    for g in range((n-R*r)//G+1):
        if r*R+g*G>n:continue
        if (n-r*R-g*G)%B==0:
            ans+=1
print(ans)
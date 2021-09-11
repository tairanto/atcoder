#!/usr/bin/python3

n,m,l=map(int,input().split())
p,q,r=map(int,input().split())
a=[i//p for i in [n,m,l]]
b=[i//q for i in [n,m,l]]
c=[i//r for i in [n,m,l]]
ans=0
for i in range(3):
    for j in range(3):
        if i==j:continue
        for k in range(3):
            if i==k or j==k:continue
            ans=max(ans,a[i]*b[j]*c[k])
print(ans)                
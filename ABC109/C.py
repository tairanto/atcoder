#!/usr/bin/python3

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

n,s=map(int,input().split())
x=list(map(int,input().split()))
x=[abs(i-s) for i in x]
ans=x[0]
for i in x[1:]:
    ans=GCD(ans,i)
print(ans)
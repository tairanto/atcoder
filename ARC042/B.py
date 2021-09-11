#!/usr/bin/python3


x0,y0=map(int,input().split())
N=int(input())
l=[list(map(int,input().split())) for _ in range(N)]
ans=float("inf")
for i in range(N):
    a,b=l[i]
    c,d=l[(i+1)%N]
    A,B,C=b-d,c-a,-d*(c-a)+c*(d-b)
    ans=min(ans,abs(A*x0+B*y0+C)/(A**2+B**2)**0.5)
print(ans)
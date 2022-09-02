#!/usr/bin/python3

N=int(input())
A,B,C=map(int,input().split())
ans=10000
for i in range(10000):
    if N-i*A<0:break
    for j in range(10000-i):
        if N-i*A-j*B<0:break
        if (N-i*A-j*B)%C==0:
            ans=min(ans,i+j+(N-i*A-j*B)//C)
print(ans)
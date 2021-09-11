#!/usr/bin/python3

N,M=map(int,input().split())
o,r,a=0,0,0
if M%2:
    r+=1
    M-=3
    N-=1
a=M//2-N
if N-a<0 or a<0:
    print(-1,-1,-1)
else:
    print(N-a,r,a)
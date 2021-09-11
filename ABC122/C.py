#!/usr/bin/python3

N,Q=map(int,input().split())
S=list(input())
c=[0]
for i in range(N-1):
    c.append(c[-1]+(S[i]+S[i+1]=="AC"))
for i in range(Q):
    l,r=map(int,input().split())
    print(c[r-1]-c[l-1])
#!/usr/bin/python3


N,K=map(int,input().split())
from math import gcd
A=[*map(int,input().split())]
G=A[0]
for i in A[1:]:
    G=gcd(G,i)
if K<=max(A) and K%G==0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
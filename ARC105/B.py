#!/usr/bin/python3
from math import gcd
n=int(input())
x=list(map(int,input().split()))
G=x[0]
for i in x[1:]:
    G=gcd(G,i)
print(G)
#!/usr/bin/python3

def lcm(x,y):
    return (x*y)//gcd(x,y)

n=int(input())
t=[int(input()) for i in range(n)]
from math import gcd
ans=1
for i in t:
    ans=lcm(ans,i)
print(ans)
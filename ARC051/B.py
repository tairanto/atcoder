#!/usr/bin/python3

count=[0]
def gcd(a,b):
    if count[0]==K:return [a,b]
    count[0]+=1
    return gcd(a+b,a)

K=int(input())
print(*gcd(1,1))

#!/usr/bin/python3

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

A,B=map(int,input().split())
gcd=GCD(A,B)
if (A//gcd)*(B//gcd)*gcd>10**18:
    print("Large")
else:
    print((A//gcd)*(B//gcd)*gcd)
#!/usr/bin/python3

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

def main():
    print(GCD(81,30))

a,b,c=map(int,input().split())
gcd=GCD(GCD(a,b),c)
print(a//gcd+b//gcd+c//gcd-3)
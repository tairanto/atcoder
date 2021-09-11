#!/usr/bin/python3

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

n,m=map(int,input().split())
s,t=input(),input()

gcd=GCD(n,m)
for i in range(gcd):
    if s[i*n//gcd]!=t[i*m//gcd]:
        print(-1)
        exit()
print(n*m//gcd)
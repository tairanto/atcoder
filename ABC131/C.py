#!/usr/bin/python3
def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b,a%b)

a,b,c,d=map(int,input().split())
print(b-a-(b//c+b//d-b//((c//GCD(c,d))*d)-(a//c+a//d-a//((c//GCD(c,d))*d)))+[0 if a%c==0 else 1][0])
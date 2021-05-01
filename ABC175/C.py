#!/usr/bin/python3
x,k,d=map(int,input().split())
x=abs(x)
if k>=x//d:
    k-=x//d
    if k%2==0:
        print(x%d)
    else:
        print(abs(x%d-d))
else:
    print(x-k*d)
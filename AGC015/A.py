#!/usr/bin/python3

n,a,b=map(int,input().split())
if b-a<0 or n-2+(a==b)<0:
    print(0)
else:
    print(1+(b-a)*(n-2))
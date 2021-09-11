#!/usr/bin/python3

x=list(map(int,input().split()))
x.sort()
print(sum(x[1:]))
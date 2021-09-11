#!/usr/bin/python3

N,M=map(int,input().split())
s=list([int(input()) for _ in range(M)])
x=set()
for i in reversed(s):
    if i in x:continue
    print(i)
    x.add(i)
for i in range(1,N+1):
    if i in x:continue
    print(i)
    x.add(i)
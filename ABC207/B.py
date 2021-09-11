#!/usr/bin/python3

A,B,C,D=map(int,input().split())
if B>=C*D:
    print(-1)
    exit()
n=0
while A>C*n*D:
    n+=1
    A+=B
print(n)
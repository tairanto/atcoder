#!/usr/bin/python3
N="".join(input().split())
n=int(input())
x=[input() for i in range(n)]
japan="0123456789"
x=[int(i.translate(str.maketrans(N,japan))) for i in x]
x.sort()
for i in x:
    print(str(i).translate(str.maketrans(japan,N)))
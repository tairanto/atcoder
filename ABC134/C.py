#!/usr/bin/python3
n=int(input())
x=[int(input()) for i in range(n)]
l,r=[0],[0]#左から、右から
for i in range(n):
    l.append(max(l[i],x[i]))
    r.append(max(r[i],x[n-1-i]))
for i in range(n):
    print(max(l[i],r[n-1-i]))
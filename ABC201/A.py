#!/usr/bin/python3
x=list(map(int,input().split()))
x.sort()
if x[2]-x[1]==x[1]-x[0]:
    print("Yes")
else:
    print("No")

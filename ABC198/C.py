#!/usr/bin/python3
r,x,y=map(int,input().split())
R=float(x**2+y**2)**0.5
if R<r:
    print(2)
else:
    print(int(R//r)+[1 if R%r else 0][0])
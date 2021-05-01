#!/usr/bin/python3
w,h,x,y=map(float,input().split())
if x==w/2 and y==h/2:
    print(w*h/2,1)
else:
    print(w*h/2,0)
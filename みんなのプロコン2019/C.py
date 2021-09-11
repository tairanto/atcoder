#!/usr/bin/python3


k,a,b=map(int,input().split())
if a+2>b or k<a:
    print(k+1)
else:
    print((((k-a-1)//2))*(b-a)+(k-a-1)%2+b)

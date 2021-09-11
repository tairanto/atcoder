#!/usr/bin/python3

a,b=input().split()
b1,b2=map(int,b.split("."))
print(int(a)*(b1*100+b2)//100)
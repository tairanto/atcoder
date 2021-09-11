#!/usr/bin/python3

n=int(input())
t=[int(input()) for i in range(5)]
m=min(t)
print(n//m+(n%m>0)-1+5)
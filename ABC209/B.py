#!/usr/bin/python3

N,X=map(int,input().split())
A=list(map(int,input().split()))
print(["Yes","No"][sum(A)-len(A)//2>X])
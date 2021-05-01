#!/usr/bin/python3
n=int(input())
x=list(map(int,input().split()))
print(sum([1 for i in range(1,n-1) if  x[i-1]<x[i]<x[i+1] or x[i-1]>x[i]>x[i+1]]))
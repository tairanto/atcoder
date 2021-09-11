#!/usr/bin/python3

n=(input())
print(sum([float(n)/(n-i+1) for i in range(2,n+1)]))
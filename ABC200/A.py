#!/usr/bin/python3
n=int(input())
print(n//100+[1 if n%100 else 0][0])
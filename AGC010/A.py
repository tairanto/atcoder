#!/usr/bin/python3

n=int(input())
if sum([1 for i in list(map(int,input().split())) if i%2])%2:
    print("NO")
else:
    print("YES")
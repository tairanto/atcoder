#!/usr/bin/python3
n=int(input())
x=list(map(int,input().split()))
if 2<sum([1 for i in range(n) if not i+1==x[i]]):
    print("NO")
else:
    print("YES")
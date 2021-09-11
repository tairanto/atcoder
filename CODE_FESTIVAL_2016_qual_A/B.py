#!/usr/bin/python3

n=int(input())
x=list(map(int,input().split()))
print(sum([1 for i in range(n) if x[x[i]-1]==i+1])//2)
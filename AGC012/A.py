#!/usr/bin/python3

n=int(input())
x=list(map(int,input().split()))
x.sort()
print(sum([x[-2-2*i] for i in range(n)]))

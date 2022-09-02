#!/usr/bin/python3

N=int(input())
A=sorted([*map(int,input().split())])
B=sorted([*map(int,input().split())])
print(sum([abs(A[i]-B[i]) for i in range(N)]))
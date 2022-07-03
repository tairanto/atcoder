#!/usr/bin/python3

N,K,Q=map(int,input().split())
mas=[0 for i in range(N+1)]
A=[*map(int,input().split())]
for i in map(int,input().split()):
    if (i==K and A[i-1]==N):continue
    if i!=K and A[i-1]+1==A[i]:continue
    A[i-1]+=1
print(*A)
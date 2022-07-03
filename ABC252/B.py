#!/usr/bin/python3

N,K=map(int,input().split())
A=[*map(int,input().split())]
B=set(map(int,input().split()))
am=max(A)
for i in range(1,N+1):
    if A[i-1]==am and i in B:
        print("Yes")
        exit()
print("No")
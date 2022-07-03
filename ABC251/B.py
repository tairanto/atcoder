#!/usr/bin/python3

N,W=map(int,input().split())
A=[*map(int,input().split())]
n=set()
for i in range(N):
    if A[i]<=W:n.add(A[i])
    for j in range(i+1,N):
        if A[i]+A[j]<=W:n.add(A[i]+A[j])
        for k in range(j+1,N):
            if A[i]+A[j]+A[k]<=W:n.add(A[i]+A[j]+A[k])
print(len(n))
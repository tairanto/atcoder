#!/usr/bin/python3

N,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
total=sum([abs(A[i]-B[i]) for i in range(N)])
if K-total<0 or (K-total)%2:
    print("No")
else:
    print("Yes")
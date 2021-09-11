#!/usr/bin/python3

import bisect
N,Q=map(int,input().split())
A=list(map(int,input().split()))
C=[0]
for i in range(N):
    C.append(A[i]-1-i)
for i in range(Q):
    K=int(input())
    index=bisect.bisect_left(C,K)
    if index>N:
        print(N+K)
    else:
        print(K+index-1)
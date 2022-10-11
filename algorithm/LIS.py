#!/usr/bin/python3

N=int(input())
A=[*map(int,input().split())]
B=[*map(int,input().split())]
seq=[0 for i in range(N)]
for i in range(N):
    seq[A[i]-1]=B[i]

import bisect

LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

print(len(LIS)+N)
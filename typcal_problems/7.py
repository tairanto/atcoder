#!/usr/bin/python3

import bisect
N=int(input())
A=sorted([*map(int,input().split())])
for i in range(int(input())):
    B=int(input())
    index = bisect.bisect_left(A, B)
    print(min(abs(A[index-1]-B),abs(A[(index)%N]-B)))

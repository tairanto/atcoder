#!/usr/bin/python3

import bisect
n,m=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
B=list(map(int,input().split()))
for i in B:
    index=bisect.bisect(A, i)
    if A:
        if A[index-1+(index==0)]>=i:
            A.pop(index-1+(index==0))
        elif index<len(A) and A[index]>=i:
            A.pop(index)
        else:
            print("NO")
            exit()
    else:
        print("NO")
        exit()
print("YES")
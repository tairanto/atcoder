#!/usr/bin/python3

N=int(input())
A=[*map(int,input().split())]
ans=0
B=sorted(A)
import bisect
for i in range(N):
    print(B)
    index=bisect.bisect_left(B, A[i])
    print(pow(2,N-index-1-i)-1)
    B.pop(index)
print(ans)
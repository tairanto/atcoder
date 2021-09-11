#!/usr/bin/python3


N,M=map(int,input().split())
A=list(map(int,input().split()))
B=sorted(list(map(int,input().split())))
print(B)
import bisect
ans=float("inf")
for i in A:
    index=bisect.bisect(B, i)
    if index==M:
        ans=min(ans,abs(i-B[index-1]))    
    else:
        ans=min(ans,abs(i-B[index]),abs(i-B[index-1]))
print(ans)
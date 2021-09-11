#!/usr/bin/python3

N=int(input())
T,A=list(input()),list(input())
ans=0.0
for i in range(1,10):
    T[4]=str(i)
    t=sum([num*10**T.count(str(num)) for num in range(1,10)])
    for j in range(1,10):
        A[4]=str(j)
        a=sum([num*10**A.count(str(num)) for num in range(1,10)])
        if t<=a:continue
        ans+=max(N-(T[:4]+A[:4]).count(str(i)),0)*max(N-(T+A[:4]).count(str(j)),0)
print(ans/((N*9-8)*(N*9-9)))
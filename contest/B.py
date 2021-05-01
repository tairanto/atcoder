#!/usr/bin/python3
a,b=map(int,input().split())
A,B=list(map(int,input().split())),list(map(int,input().split()))
x=[0 for i in range(10**3+1)]
for i in A:x[i]+=1
for i in B:x[i]+=1
ans=[i for i in range(10**3+1) if x[i]==1]
print(*ans)
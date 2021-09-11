#!/usr/bin/python3

N,Q=map(int,input().split())
ans=[0 for i in range(N+1)]
same=set()
for i in range(Q):
    l,r=map(int,input().split())
    ans[l-1]+=1
    ans[r]-=1
n=0
for i in ans[:-1]:
    n+=i
    print(n%2,end="")
print()
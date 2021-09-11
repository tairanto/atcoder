#!/usr/bin/python3

n,k,s=map(int,input().split())
ans=[]
if s==10**9:
    print(*([s]*k+[s-1]*(n-k)))
else:
    print(*([s]*k+[s+1]*(n-k)))
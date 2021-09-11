#!/usr/bin/python3
import itertools
n=int(input())
p = itertools.permutations([i+1 for i in range(n)], n)
P,Q=list(map(int,input().split())),list(map(int,input().split()))
ans=[0,0]
for x,i in enumerate(p):
    temp=list(i)
    if P==temp:ans[0]=x
    if Q==temp:ans[1]=x
print(abs(ans[0]-ans[1]))
#!/usr/bin/python3

N=int(input())
ans=set()
for i in range(N):
    ans.add(tuple(map(int,input().split())))
print(len(ans))
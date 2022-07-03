#!/usr/bin/python3

N=int(input())
ans={}
ori=set()
for i in range(N):
    s,t=input().split()
    if s in ori:continue
    ori.add(s)
    if int(t) in ans:continue
    ans[int(t)]=i+1
print(ans[max(ans)])
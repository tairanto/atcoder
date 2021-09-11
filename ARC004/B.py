#!/usr/bin/python3

N=int(input())
d=[int(input()) for i in range(N)]
ans=max(max(d)*2-sum(d),0)
print(sum(d),ans,sep="\n")
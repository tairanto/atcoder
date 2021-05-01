#!/usr/bin/python3
n,k=map(int,input().split())
s=list(input())
s[k-1]=s[k-1].lower()
print(*s,sep="")
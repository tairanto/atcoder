#!/usr/bin/python3
n,l=map(int,input().split())
cnt,m=0,1000
for i in range(n):
    if abs(m)>abs(l+i):m=l+i
    cnt+=l+i
print(cnt-m)
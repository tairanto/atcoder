#!/usr/bin/python3

n,k=map(int,input().split())
a=list(map(int,input().split()))
print(1+(n-k)//(k-1)+((n-k)%(k-1)>0))
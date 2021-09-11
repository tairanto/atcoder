#!/usr/bin/python3

k,n=map(int,input().split())
print(*[i for i in range(n-k+1,n+k)])
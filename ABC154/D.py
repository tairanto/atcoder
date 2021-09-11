#!/usr/bin/python3

n,k=map(int,input().split())
p=list(map(int,input().split()))
c=[sum(p[:k])]
for i in range(1,n-k+1):
    c.append(c[-1]-p[i-1]+p[k+i-1])
print((max(c)+k)/2)
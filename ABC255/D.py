#!/usr/bin/python3

import bisect
N,Q=map(int,input().split())
A=sorted([*map(int,input().split())])
stock=[0]
for i in A:
    stock.append(stock[-1]+i)
for i in range(Q):
    q=int(input())
    num=bisect.bisect_right(A,q)
    print(num*q-stock[num]-(N-num)*q+stock[-1]-stock[num])
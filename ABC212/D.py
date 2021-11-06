#!/usr/bin/python3

import heapq

a = []
heapq.heapify(a)
Q=int(input())
Sum=0
for i in range(Q):
    temp=input()
    if temp[0]=="3":
        print(heapq.heappop(a)+Sum)
    else:
        p,x=map(int,temp.split())
        if p==1:
            heapq.heappush(a,x-Sum)
        else:
            Sum+=x
#!/usr/bin/python3

N=int(input())
import heapq  # heapqライブラリのimport
from collections import deque
temp=deque()
a = []
heapq.heapify(a)  # リストを優先度付きキューへ
for i in range(N):
    x=input().split()
    if len(x)==2:
        temp.append(int(x[1]))
    else:
        if x[0]=="2":
            if a:
                print(heapq.heappop(a))
            else:
                print(temp.popleft())
        else:
            [heapq.heappush(a, i) for i in temp]
            temp=deque()
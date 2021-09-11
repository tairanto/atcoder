#!/usr/bin/python3

n=int(input())
import heapq  # heapqライブラリのimport
x = [int(input())]
heapq.heapify(x)  # リストを優先度付きキューへ
flag=1
m=0
for i in range(n-1):
    if flag:
        temp=heapq.heappop(x) # 最小値の取り出し
        flag=0
    num=int(input())
    if temp<num:
        temp=num
        m=1
    else:
        heapq.heappush(x, temp)
        temp=heapq.heappop(x)
        if temp<num:
            temp=num
            continue
        heapq.heappush(x, temp)
        heapq.heappush(x, num)
        flag=1
if m:
    print(len(x)+1)
else:
    print(len(x))
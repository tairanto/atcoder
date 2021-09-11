#!/usr/bin/python3


import heapq  # heapqライブラリのimport

a = []
heapq.heapify(a)  # リストを優先度付きキューへ
heapq.heappop(a)  # 最小値の取り出し
heapq.heappush(a, -2)  # 要素の挿入

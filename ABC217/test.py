#!/usr/bin/python3

import bisect
L,Q=map(int,input().split())
cut=[0,L]
for i in range(Q):
    c,x=map(int,input().split())
    index=bisect.bisect_left(cut, x)
    if c==1:
        cut.insert(index,x)
    else:
        print(cut[index]-cut[index-1])

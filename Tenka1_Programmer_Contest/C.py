#!/usr/bin/python3

N=int(input())
for h in range(1,3501):
    for n in range(1,3501):
        if not (4*h*n-N*n-N*h):continue
        w=(N*h*n)//(4*h*n-N*n-N*h)
        if w>0 and (N*h*n)%(4*h*n-N*n-N*h)==0:
            print(h,n,w)
            exit()
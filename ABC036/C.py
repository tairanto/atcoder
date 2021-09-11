#!/usr/bin/python3


N=int(input())
a=[int(input()) for i in range(N)]
num={i:x for x,i in enumerate(sorted(list(set(a))))}
for i in a:
    print(num[i])
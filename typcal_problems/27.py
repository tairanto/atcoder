#!/usr/bin/python3

N=int(input())
s=set()
for i in range(N):
    S=input()
    if not S in s:
        s.add(S)
        print(i+1)
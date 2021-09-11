#!/usr/bin/python3

N=int(input())
s=set()
for i in range(N):
    s.add(input())
for i in s:
    if "!"+i in s:
        print(i)
        exit()
print("satisfiable")
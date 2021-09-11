#!/usr/bin/python3

N=int(input())
name=set()
for i in range(N):
    temp=input()
    if temp in name:continue
    name.add(temp)
    print(i+1)
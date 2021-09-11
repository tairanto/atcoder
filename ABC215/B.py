#!/usr/bin/python3

N=int(input())
for i in range(60,-1,-1):
    if pow(2,i)<=N:
        print(i)
        exit()
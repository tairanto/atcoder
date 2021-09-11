#!/usr/bin/python3

N=int(input())
for i in range(int(N**0.5),0,-1):
    if N%i==0:
        print(len(str(max(i,N//i))))
        exit()
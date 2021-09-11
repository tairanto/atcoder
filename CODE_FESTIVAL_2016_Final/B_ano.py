#!/usr/bin/python3

N=int(input())
for i in range(1,N+1):
    score=i*(i+1)//2
    if score>=N:
        break
for i in range(1,i+1):
    if score-N==i:continue
    print(i)
#!/usr/bin/python3

n=int(input())
A=list(map(int,input().split()))
q=int(input())
num={i+1:0 for i in range(10**5)}
total=sum(A)
for i in A:
    num[i]+=1
for i in range(q):
    B,C=map(int,input().split())
    total+=(C-B)*num[B]
    num[C]+=num[B]
    num[B]=0
    print(total)

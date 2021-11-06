#!/usr/bin/python3


N=int(input())
A=[i-x-1 for x,i in enumerate(map(int,input().split()))]
A.sort()
if N%2:b=A[N//2]
else:b=(A[N//2-1]+A[N//2])//2
print(sum([abs(i-b) for i in A]))
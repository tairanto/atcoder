#!/usr/bin/python3
n=int(input())
x=list(map(int,input().split()))
A=int(input())
num=[[0] for i in range(n+1)]
num[0]+=[0 for i in range(A)]
print(num)
for i in range(n):
    for j in range(1,A+1):
        if j>=x[i]:num[i+1].append(max(num[i][j-x[i]]+x[i],num[i][j]))
        else:num[i+1].append(num[i][j])
print(num)
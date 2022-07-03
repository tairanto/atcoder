#!/usr/bin/python3

N,K=map(int,input().split())
A=[*map(int,input().split())]
B=sorted(A)
num={}
for i in range(N):
    if not A[i] in num:
        num[A[i]]=[set(),set()]
    if not B[i] in num:
        num[B[i]]=[set(),set()]
    num[A[i]][0].add(i)
    num[B[i]][1].add(i)
for i in num:
    flag=0
    for j in list(num[i][0]):
        for k in list(num[i][1]):
            if abs(j-k)%K==0:
                num[i][0].remove(j)
                num[i][1].remove(k)
                break
    if len(num[i][0]):
        print("No")
        exit()
print("Yes")
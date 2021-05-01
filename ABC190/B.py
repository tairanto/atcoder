#!/usr/bin/python3
n,m=map(int,input().split())
ab=[list(map(int,input().split())) for i in range(m)]
k=int(input())
cd=[list(map(int,input().split())) for i in range(k)]
bit=[bin(i)[2:].zfill(k) for i in range(2**k)]
M=0
for i in bit:
    count=0
    temp=[0 for j in range(n)]
    for c,j in enumerate(list(i)):
        temp[cd[c][int(j)]-1]+=1
    for j in ab:
        if temp[j[0]-1]>0 and temp[j[1]-1]>0:
            count+=1
    if M<count:
        M=count
print(M)
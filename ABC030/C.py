#!/usr/bin/python3


N,M=map(int,input().split())
X,Y=map(int,input().split())
A=[*map(int,input().split())]
B=[*map(int,input().split())]
now=0
a,b=0,0
time=0
while a<N and b<M:
    if now%2:#B
        if B[b]>=time:
            time=B[b]+Y
            now+=1
        else:
            b+=1
    else:#A
        if A[a]>=time:
            time=A[a]+X
            now+=1
        else:
            a+=1
print(now//2)
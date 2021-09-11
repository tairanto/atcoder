#!/usr/bin/python3

n=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
a,c={},{}
for i in A:
    if not i in a:
        a[i]=0
    a[i]+=1
for i in C:
    if not i in c:
        c[i]=0
    c[i]+=1
cnt=0
for i in c:
    if B[i-1] in a:
        cnt+=c[i]*a[B[i-1]]
print(cnt)
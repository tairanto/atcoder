#!/usr/bin/python3

n=int(input())
B=list(map(int,input().split()))
B0=B[0]
B=[i-B0 for i in B]
A=[B0]
temp=[list(map(int,input().split())) for i in range(n-1)]
for i in range(n-1):
    for j in range(n):
        if B[j]+temp[i][0]!=temp[i][j]:
            print("No")
            exit()
    A.append(temp[i][0])
m=min(B)
if m<0:
    A=[i+m for i in A]
    B=[i-m for i in B]
print("Yes")
print(*A)
print(*B)
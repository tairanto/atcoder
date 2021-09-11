#!/usr/bin/python3


n=int(input())
x=list(map(int,input().split()))
x.sort()
for i in range(1,n+1):
    if i!=x[i-1]:
        print("No")
        exit()
print("Yes")
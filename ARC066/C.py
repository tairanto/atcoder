#!/usr/bin/python3

N=int(input())
A=[*map(int,input().split())]
a={2*i+(N%2==0):2 for i in range((N+1)//2)}
if N%2:a[0]=1
for i in A:
    if not i in a:
        print(0)
        exit()
    a[i]-=1
    if a[i]==-1:
        print(0)
        exit()
print(pow(2,N//2,10**9+7))